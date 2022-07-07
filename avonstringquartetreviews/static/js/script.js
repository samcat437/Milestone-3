document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    var datepicker= document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker);
  });