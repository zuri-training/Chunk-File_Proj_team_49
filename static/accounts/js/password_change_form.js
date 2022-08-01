
const form = document.getElementById('form')
const currentPassword = document.getElementById('current-password');
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
	const currentPsswordValue = currentPassword.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	
	
	if(currentPsswordValue === '') {
		setErrorFor(currentPassword, 'Full Name cannot be blank');
	}else if(currentPsswordValue.length < 7){
		setErrorFor(currentPassword, 'Full Name must be more than 6 letters');
	}else if(currentPsswordValue.length > 20){
		setErrorFor(currentPassword, 'Full name must be less than 15');
	}
	 else {
		setSuccessFor(currentPassword);
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

  function relocate_home()
{
     location.href = "dashboard.html";
} 
