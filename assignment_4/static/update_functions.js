function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("usersListToUpdateID");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}




 function show() {
                var rowId =
                    event.target.parentNode.parentNode.id;
              //this gives id of tr whose button was clicked
                var data =
              document.getElementById(rowId).querySelectorAll(".row-data");
              /*returns array of all elements with
              "row-data" class within the row with given id*/
                var ID = data[0].innerHTML;
                var name = data[1].innerHTML;
                var nickName = data[2].innerHTML;
                var Email = data[3].innerHTML;
                var Gender = data[4].innerHTML;
                var Age = data[5].innerHTML;
                var Password = data[6].innerHTML;
                document.getElementById('id01').style.display='block'
                document.getElementById('replace-me').innerText =
                    ( "User ID: " + ID + "\nName: " + name + "\nnickName: " + nickName + "\nEmail: " + Email + "\nGender: " + Gender + "\nAge: " + Age + "\nPassword: " + Password)
                document.getElementById('userID_ID').value = ID.replaceAll(" ", "");


            }

// success alert close window function
function closeFunction(){
    alertDiv= document.getElementById('alertDiv')
    alertDiv.style.display = "none";
}


