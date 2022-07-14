document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav, {edge: 'right'});
    var datepicker= document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker);
  });


        