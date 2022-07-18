document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav, {edge: 'right'});
    let timepicker = document.querySelectorAll('.timepicker');
    M.Timepicker.init(timepicker);
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker);
   
    let modals = document.querySelectorAll('.modal');
    let instances = M.Modal.init(modals);

    for (modal of instances) {
    modal.open();
    }    

    // not working 
    // let helperplaceholder = document.getElementsByClassName("helper-placeholder");
    // helperplaceholder.addEventListener("click", () => {
    //   helperplaceholder.classList.add("hidden");
    // })
  });


        