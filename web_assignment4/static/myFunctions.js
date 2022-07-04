var i = 0;
var txt = 'Please fill out all required fields.';
var speed = 50;
var deg= 2;



const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
    if(link.href.includes(`${activePage}`)){

     console.log(activePage);
          console.log(link.href);

      link.classList.add('active');
    }
  });


  
function typeWriter() {
    
    if (i < txt.length) {
        document.getElementById("errorMessage").innerHTML += txt.charAt(i);
        rotateFun(i);
        i++;
        setTimeout(typeWriter, speed);
        }
      }

      function rotateFun(i){
        const elements1 =document.getElementsByTagName('input');
        for (var j = 0; j<6; j++){
            if(i<2){
                elements1[j].style.transform="rotate(-2deg)";}
                if(i>=2 && i<4){
                    elements1[j].style.transform="rotate(2deg)";}
                if(i>=4 && i<6){
                    elements1[j].style.transform="rotate(-2deg)";}
                if(i>=6 && i<8){
                    elements1[j].style.transform="rotate(2deg)";}
                if(i>=8){
                    elements1[j].style.transform="rotate(0deg)";}
        }

      }


      function showLoadMoreImg(){
        document.getElementById("galleryLoadMoreID").style.display = "grid";
        document.getElementById("loadMorebutton").style.display = "none";
        document.getElementById("showLass").style.display = "table";

      }

      function showLassImg(){
        document.getElementById("galleryLoadMoreID").style.display = "none";
        document.getElementById("loadMorebutton").style.display = "table";
        document.getElementById("showLass").style.display = "none";

      }

