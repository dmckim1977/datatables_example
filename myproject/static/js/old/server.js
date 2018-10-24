
$(document).ready(function() {
    $('#example').dataTable( {
        "bProcessing": true,
        "bServerSide": true,
        "sAjaxSource": {url: 'http://127.0.0.1:8000/datatable/',
         dataSrc: 'http://127.0.0.1:8000/invoices/DT-browser-default/'}
    } );
} );