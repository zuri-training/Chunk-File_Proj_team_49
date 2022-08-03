//Button When clicked starts here!

const active = document.getElementById('active');

active.addEventListener('click', function onClick() {
  active.style.backgroundColor = '#251561';
  active.style.border = '1px solid #000000';
});

const seconBtn = document.getElementById('seconBtn');

seconBtn.addEventListener('click', function onClick() {
  seconBtn.style.border = '2px solid #FCC6C6';
});

const secBtn = document.getElementById('secBtn');

secBtn.addEventListener('click', function onClick() {
  secBtn.style.backgroundColor = '#251561';
  secBtn.style.border = '1px solid ';
});

//Button When clicked ends here!


//Button When disabled starts here!
const subScribe = document.getElementById('subScribe');
const input = document.getElementById('newsLetter')

subScribe.addEventListener('click', function onClick() {
  subScribe.style.border = '2px solid #FCC6C6';
});
input.addEventListener("keyup", (e) => {
  const value = e.currentTarget.value;
  subScribe.disabled = false;

  if (value === ""){
    subScribe.disabled = true;
  }
  if (subScribe.disabled === true){
    subScribe.style.backgroundColor ='#E1E1E1';
    subScribe.style.border ='#FCC6C6';
  }
  if (subScribe.disabled === false){
    subScribe.style.backgroundColor ='#FAA9A9';
  }
})
