const nav = document.querySelector(".ham-btn");
const x = document.querySelector(".navigation");
const y = document.querySelector(".close-btn");
const navbar = document.querySelector("#navbar");
console.log(x);
function closeNav(e) {
  e.preventDefault();
  x.style.display = "flex";
  if (y.style.display === "block") {
    x.style.display = "none";
    y.style.display = "none";
    nav.style.display = "block";
  }
}

function displayNav(e) {
  e.preventDefault();
  if (x.style.display === "flex") {
    x.style.display = "none";
  } else {
    x.style.display = "inline-block";
    nav.style.display = "none";
    y.style.display = "block";
  }
}

nav.addEventListener("click", displayNav);
y.addEventListener("click", closeNav);
