// function confirmationMessage() {

//   let deleteOne = document.getElementById("delete");
//   deleteOne.addEventListener("click", () => {
//     deleteOne.ClassList.add("selected");
//     console.log("selected");
//   });
// }


document.addEventListener('DOMContentLoaded', function() {
    console.log("hello")
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav, {edge: 'right'});
    let timepicker = document.querySelectorAll('.timepicker');
    M.Timepicker.init(timepicker);
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker);
   
    let modals = document.querySelectorAll('.modal');
    var instances = M.Modal.init(modals);
    console.log(instances)
    // for (modal of instances) {
    // console.log("Hello")
    // modal.open();
    // }    

    // not working 
    // let helperplaceholder = document.getElementsByClassName("helper-placeholder");
    // helperplaceholder.addEventListener("click", () => {
    //   helperplaceholder.classList.add("hidden");
    // })
  });


        