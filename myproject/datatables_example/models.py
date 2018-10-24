from django.db import models
from datetime import datetime

class Invoice(models.Model):
    invoice_number =                models.IntegerField(null=True, blank=True, unique=True)
    invoice_date =                  models.DateTimeField(null=True, blank=True)
    bill_name =                     models.CharField(max_length=255, null=True, blank=True)
    rental_ticket_or_tag_number =   models.IntegerField(default=0)
    order_date =                    models.DateTimeField(null=True, blank=True)
    closed_date =                   models.DateTimeField(null=True, blank=True)
    ordered_by =                    models.CharField(max_length=255, null=True, blank=True)
    closed_flag =                   models.NullBooleanField(default=0)
    job_type =                      models.CharField(max_length=255, null=True, blank=True)
    delivered_by =                  models.CharField(max_length=255, null=True, blank=True)
    well_name =                     models.CharField(max_length=255, null=True, blank=True)
    contractor =                    models.CharField(max_length=255,null=True, blank=True)
    dispatcher =                    models.CharField(max_length=255, null=True, blank=True)
    field_rental_ticket =           models.CharField(max_length=255, null=True, blank=True)
    creation_date =                 models.DateTimeField(null=True, blank=True)
    date_to_start_billing =         models.DateTimeField(null=True, blank=True)
    date_to_stop_billing =          models.DateTimeField(null=True, blank=True)
    last_modification_date =        models.DateTimeField(null=True, blank=True)
    invoice_office_code =           models.CharField(max_length=100, null=True, blank=True)
    printed_flag =                  models.NullBooleanField(default=0)
    repair_invoice_flag =           models.NullBooleanField(default=0)
    invoice_pre_tax_total =         models.DecimalField(max_digits=8,
                                                        decimal_places=2,
                                                        null=True,
                                                        blank=True)
    invoice_total =                 models.DecimalField(max_digits=8,
                                                        decimal_places=2,
                                                        null=True,
                                                        blank=True)
    date_sent_for_signature =       models.DateField(null=True, blank=True)

    EMAILED = 'EMA'
    SALESMAN = 'SAL'
    METHOD = (
        ('EMA', 'EMAILED'),
        ('SAL', 'SALESMAN'),
    )

    method_sent =                   models.CharField(max_length=3,
                                                       choices=METHOD,
                                                       null=True,
                                                       blank=True)
    person_sent_with_invoice =      models.CharField(max_length=255, null=True, blank=True)
    date_signed_invoice_returned =  models.DateField(null=True, blank=True)
    date_submitted =                models.DateField(null=True, blank=True)
    notes =                         models.TextField(null=True, blank=True)
    is_void =                       models.NullBooleanField(null=True, blank=True)
    is_paid =                       models.NullBooleanField(null=True, blank=True)

    def __str__(self):
        return '{} {}' .format(self.invoice_number, self.notes)

    @property
    def get_submitted_age(self):
        if self.date_submitted:
            submitted_age = self.date_submitted - datetime.datetime.now()
        else:
            submitted_age = ''
        return submitted_age
