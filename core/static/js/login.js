const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});


function togglePasswordVisibility(passwordInputId, toggleIconId) {
    const passwordInput = document.getElementById(passwordInputId);
    const toggleIcon = document.getElementById(toggleIconId);
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    toggleIcon.classList.toggle('fa-eye');
    toggleIcon.classList.toggle('fa-eye-slash');
}

document.getElementById('toggle-signup-password').addEventListener('click', function () {
    togglePasswordVisibility('signup-password', 'toggle-signup-password');
});

document.getElementById('toggle-signin-password').addEventListener('click', function () {
    togglePasswordVisibility('signin-password', 'toggle-signin-password');
});