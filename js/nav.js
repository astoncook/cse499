const hambutton = document.querySelector('.menu');
const mainnav = document.querySelector('.navigation')

hambutton.addEventListener('click', () => {mainnav.classList.toggle('responsive')}, false);

// To solve the mid resizing issue with responsive class on
window.onresize = () => {if (window.innerWidth > 760) mainnav.classList.remove('responsive')};

const links = document.querySelectorAll("#nav li a");
const page = document.querySelector("#page");

links.forEach( function(e) {
	e.addEventListener("click", function() {
    let goToPage = e.dataset.page;
    $("#page").load(goToPage + ".php");
  });
});