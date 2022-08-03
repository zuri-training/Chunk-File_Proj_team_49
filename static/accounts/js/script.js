const form = document.getElementById('form')
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
	checkInputs();
	if(validForm() == true) {
		form.submit ();
	} else {
		e.preventDefault();
	}
});

function validForm() {
	const inputContainers = form.querySelectorAll('.input-control');
	let result = true;

	inputContainers.forEach((container) => {
		if(container.classList.contains('error')){
			result  = false;
		}
	});
	return result;
}

function checkInputs() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	
	
	if(usernameValue === '') {
		setErrorFor(username, 'Full Name cannot be blank');
	}else if(usernameValue.length < 7){
		setErrorFor(username, 'Full Name must be more than 6 letters');
	}else if(usernameValue.length > 20){
		setErrorFor(username, 'Full name must be less than 15');
	}
	 else {
		setSuccessFor(username);
	}
	
	if(emailValue === '') {
		setErrorFor(email, 'Email cannot be blank');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Not a valid email');
	} else {
		setSuccessFor(email);
	}
	
	if(passwordValue === '') {
		setErrorFor(password, 'Password cannot be blank');
	}else if(passwordValue.length < 8){
		setErrorFor(password, 'password can not be less than 8');
	}
	 else {
		setSuccessFor(password);
	}
	
	if(password2Value === '') {
		setErrorFor(password2, 'Confirm password cannot be blank');
	}else if(password2Value.length < 8){
		setErrorFor(password2, 'password can not be less than 8');
	}else if(passwordValue !== password2Value) {
		setErrorFor(password2, 'Passwords do not match');
	} else{
		setSuccessFor(password2);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'input-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'input-control success';
}
	
function isEmail(email) {

	const checkemail = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
	const emailResult = checkemail.test(email);
	return emailResult

}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()

  function relocate_home()
{
     location.href = "login.html";
} 