from datetime import date
from rest_framework import serializers

from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField(format="%m-%d-%Y %H:%M")
    date_sent_for_signature = serializers.DateTimeField(format="%m-%d-%Y")
    date_signed_invoice_returned = serializers.DateTimeField(format="%m-%d-%Y")
    date_submitted = serializers.DateTimeField(format="%m-%d-%Y")
    submitted_age = serializers.SerializerMethodField()
    dro = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ('id', 'invoice_number', 'bill_name', 'ordered_by', 'job_type',
                  'well_name', 'contractor', 'creation_date', 'invoice_office_code',
                  'invoice_total', 'date_sent_for_signature', 'method_sent',
                  'person_sent_with_invoice', 'date_signed_invoice_returned',
                  'date_submitted', 'submitted_age', 'dro', 'notes', 'is_paid', 'is_void')
        extra_kwargs = {'method_sent': {'required': False}}

    def get_submitted_age(self, obj):
        # this is just business logic I needed but I left in the serializer so I didn't have to change a lot of stuff
        if obj.date_submitted:
            aging = date.today() - obj.date_submitted
            return aging.days

    def get_dro(self, obj):
        # this is just business logic I needed but I left in the serializer so I didn't have to change a lot of stuff
        if obj.date_submitted:
            dro = obj.date_submitted - obj.creation_date.date()
            return dro.days
        else:
            dro = date.today() - obj.creation_date.date()
            return dro.days
