const faqList = [
  {
    id: 1,
    title: "How can I use Chunk49?",
    description:
      "Simply upload your file to Chunk 49, open your file, and you're on your way. No installation, database, or configuration required. Chunk 49 gives you access to extraordinary big data insights in minutes, not hours.",
  },
  {
    id: 2,
    title: "Is my data secure?",
    description:
      "Chunk 49 uses a combination of encryption and technical safeguards to protect our customers’ data. Our privacy obligations and the protection of your information is not taken lightly, and we comply with all applicable privacy laws and regulations.",
  },
  {
    id: 3,
    title: "What is Chunk 49?",
    description:
      "CHUNK 49 is a platform that accepts large CSV or JSON files and splits them into smaller bits while maintaining the output in the same format",
  },
  {
    id: 4,
    title: "What user information does Chunk 49 store?",
    description:
      "Beyond user financial information required for billing purposes, and user emails and passwords to allow access to the service, Chunk 49 stores the following user data: Original uploaded files parsed uploaded files uploaded file metadata such as file size and file name",
  },
  {
    id: 5,
    title: " Can i save my files to download them later?",
    description: "Yes you can save your files to download them later.",
  },
];

let contTitle = document.querySelectorAll(".content-title");
let contDescription = document.querySelectorAll(".content-description");
let contid = document.querySelectorAll(".content-title").textContent;
console.log(contTitle);
const contentArr = faqList.map((item) => {
  for (let a = 0; a <= contTitle.length; a++) {
    if (a + 1 === item.id) {
      contTitle[a].innerHTML = item.title;
      contDescription[a].innerHTML = item.description;
    }
  }
});

const nav = document.querySelector(".ham-btn");
const x = document.querySelector(".navigation");
const y = document.querySelector(".close-btn");
const navbar = document.querySelector("#navbar");
console.log(x);
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
function closeNav(e) {
  e.preventDefault();
  x.style.display = "flex";
  if (y.style.display === "block") {
    x.style.display = "none";
    y.style.display = "none";
    nav.style.display = "block";
  }
}

nav.addEventListener("click", displayNav);
y.addEventListener("click", closeNav);
