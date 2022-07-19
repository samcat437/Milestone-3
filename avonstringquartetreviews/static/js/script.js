document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav, {edge: 'right'});
    let timepicker = document.querySelectorAll('.timepicker');
    M.Timepicker.init(timepicker);
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker);
   
    let modals = document.querySelectorAll('.modal');
    var instances = M.Modal.init(modals);
    console.log(instances);
  });      