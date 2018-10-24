from django.conf.urls import url
from . import views


app_name = 'invoice'
urlpatterns = [
    # api views
    url(r'^api/unpaid_invoices/$', views.InvoiceList.as_view(), name='invoice-list'), # ajax link to load populate the datatable

    # template views
    url(r'^unpaid_invoices/', views.TemplateView.as_view(template_name="datatables_example/unpaid_invoices.html")), # loads the template
    url(r'^invoices/(?P<pk>[0-9]+)/$', views.InvoiceDetail, name='invoice-detail'), # view to get and post changed to the database with datatables editor

]
