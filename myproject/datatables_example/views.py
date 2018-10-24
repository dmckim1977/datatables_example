import json
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from rest_framework import generics

from .models import Invoice
from . import parser

from .serializers import InvoiceSerializer


class InvoiceList(generics.ListCreateAPIView):
    '''
    View to get the list of invoice objects from the database.

    The serializer is used to create json that datatables can read.
    '''
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    raise_exception = True # creates an exception that datatables can show in the table


def InvoiceDetail(request, pk):
    """
    View to POST and GET detail data from the database.

    I am not proud of this function but it mostly works the way I want.
    You will not be able to blank out a value in the datatables editor because my code below ignores empty strings so
    you do not overwrite existing data in the database. If you want to 'erase' data in datatables editor with this code
    then you need to enter a string with a space. ie: ' '
    """
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'PUT':
        # this is when you make changes with datatables editor. I think there was a reason I used PUT instead of POST
        # but I cant remember why that was right now.
        #change pk to an int
        pk = int(pk)

        # parse request querydict into dict
        # I could not find a better way to do this.
        data = parser.parse(request.body)

        # extract out the nested dict needed for drf post
        # datatables always send it nested in 'data' but you can change that if you want to
        parsed_data = data['data'][pk]

        for key, val in parsed_data.items():
            # this is the ugliest part of the function
            # This looks at every value in the dictionary and if it is an empty string then it skips it.
            # An empty string means there wasn't a change
            # If it has data if will go through the keys until it gets a match and then update that in the database
            # The problem is I don't want it to update everything because if there was no change it will send a blank string
            # and then it could overwrite an existing value in the database with a blank string.
            if key in parsed_data:
                if val == '':
                    continue
                else:
                    if key == 'notes':
                        Invoice.objects.filter(pk=pk).update(notes=val)
                    if key == 'date_sent_for_signature':
                        Invoice.objects.filter(pk=pk).update(
                            date_sent_for_signature=val)
                    if key == 'method_sent':
                        Invoice.objects.filter(pk=pk).update(method_sent=val)
                    if key == 'person_sent_with_invoice':
                        Invoice.objects.filter(pk=pk).update(
                            person_sent_with_invoice=val)
                    if key == 'date_signed_invoice_returned':
                        Invoice.objects.filter(pk=pk).update(
                            date_signed_invoice_returned=val)
                    if key == 'date_submitted':
                        Invoice.objects.filter(pk=pk).update(
                            date_submitted=val
                        )

        # After making a change in the database you will need to send the data back to datatables
        # If it doesn't match what datatables sends then it will not refresh the datatable
        # this code formats everything to match what datatables send in the PUT request
        parsed_data['id'] = str(pk)

        serializer = InvoiceSerializer(
            Invoice.objects.filter(pk=pk), many=True)
        data = serializer.data

        # This will nest it back into the 'data' dict
        data_dict = {'data': data}
        json_data = json.dumps(data_dict)

        return HttpResponse(json_data)


