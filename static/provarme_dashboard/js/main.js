$(function () {
  $("#datatable").DataTable( {
     "language": {
      "url": "https://cdn.datatables.net/plug-ins/1.10.12/i18n/Portuguese-Brasil.json"
    }
  });

  var clipboard = new ClipboardJS(".copy");

  clipboard.on("success", function(e) {
    toastr.success("", "Link copiado!");
    e.clearSelection();
  });

  $(".date").mask("99/99/9999");
  $(".date").datepicker({
    uiLibrary: "bootstrap4",
    format: "dd/mm/yyyy",
    locale: "pt-br",
  });

  $(".money").maskMoney({
    allowNegative: false,
    thousands: ".",
    decimal: ",",
    affixesStay: false
  });

})
