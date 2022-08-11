const form = document.getElementById('form__div')
const email = document.getElementById('email');
const password = document.getElementById('password');

form.addEventListener('submit', e => {
	e.preventDefault();
	
	checkInputs();
});


function checkInputs() {
	// trim to remove the whitespaces
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	
	if(emailValue === '') {
		setErrorFor(email, 'Email cannot be empty');
	}
	else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Looks like this is not an email');

	} else {
        setSuccessFor(email)
	} 
	
	if(passwordValue === '') {
		setErrorFor(password, 'Password cannot be empty');
	} else {
        setSuccessFor(password)
	}
	
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form';
}
	
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

