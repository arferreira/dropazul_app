$(function () {
  $('#datatable').DataTable( {
     "language": {
      "url": "https://cdn.datatables.net/plug-ins/1.10.12/i18n/Portuguese-Brasil.json"
    }
  });

  var clipboard = new ClipboardJS('.copy');

  clipboard.on('success', function(e) {
    toastr.success('', 'Link copiado!');
    e.clearSelection();
  });

})
