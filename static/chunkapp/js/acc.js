const nav = document.querySelector(".ham-btn");
const x = document.querySelector(".navigation");
const screenwidth = document.documentElement.clientWidth;
console.log(screenwidth);

console.log(x);
function displayNav(e) {
  e.preventDefault();
  if (x.style.display === "flex") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
  return;
}

nav.addEventListener("click", displayNav);
