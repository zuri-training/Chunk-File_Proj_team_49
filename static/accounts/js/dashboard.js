// check for valid csv and jsv file extension
function validateUploadedFile(event) {
    const file = event.target.files[0]
    const validFile = validateInput(file)
    if (!validFile) {
        const doc = document.getElementById("file-error")
        doc.classList.toggle("hide")
        const submitBtn = document.getElementById("submit")
        submitBtn.setAttribute('disabled', 'disabled')
        setTimeout(() => {
            doc.classList.toggle("hide")
        }, 4000);
    } else {
        const doc = document.getElementById("file-name")
        const submitBtn = document.getElementById("submit")
        submitBtn.removeAttribute('disabled')
        doc.textContent = file.name
    }
}

function validateInput(file) {
    if ((file.type === "application/json") || (file.type === "text/csv")) {
        return true
    } else {
        return false
    }
}
// ------------------------------------------------------------------------
// const upload = () => {
//     const progressBar = document.querySelector('.progress-bar')
//     progressBar.setAttribute('id', 'play-animation')
// }
// ------------------------------------------------------------------------


//Increment or decrement selet button
let number = document.querySelector('[name="number"]');

function inc() {
    let number = document.querySelector('[name="number"]');
    number.value = parseInt(number.value) + 1;
}

function dec() {
    let number = document.querySelector('[name="number"]');
    if (parseInt(number.value) > 0) {
        number.value = parseInt(number.value) - 1;
    }
}
// disabling the sumbit button till input is valid
function validateInputNumber() {
    const noOfLines = document.getElementById('number').value
    let submitBtn = document.getElementById('submit')
    parseInt(noOfLines)
    if (noOfLines <= 0) {
        submitBtn.setAttribute('disabled', 'disabled')
        console.log('Invalid');
    } else {
        submitBtn.removeAttribute('disabled')
        console.log('valid');
    }
}


// setting link active
function clickLinkA(li) {
    items = document.querySelectorAll('.list.active');

    if (items.length > 0) {
        items[0].classList.remove('active');
    }

    li.classList.add('list', 'active');
}

// dashboard sidebar toggle
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar')
    sidebar.classList.toggle('d-none')
}