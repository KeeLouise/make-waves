// Automatically fade out alerts after 4 seconds - KR 22/05/2025
setTimeout(function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    });
}, 3000);

// Registration form validation - KR 30/05/2025
document.addEventListener('DOMContentLoaded', function () {
  const registerForm = document.querySelector('#registerForm form');
  if (registerForm) {
    registerForm.addEventListener('submit', function (e) {
      const email = document.querySelector('#reg-email');
      const password = document.querySelector('#reg-password');
      const firstName = document.querySelector('#first_name');
      const surname = document.querySelector('#surname');

      let valid = true;
      let message = '';

      if (!email.value.includes('@')) {
        valid = false;
        message += 'Invalid email format.\n';
      }

      if (password.value.length < 6) {
        valid = false;
        message += 'Password must be at least 6 characters.\n';
      }

      if (!firstName.value.trim()) {
        valid = false;
        message += 'First name is required.\n';
      }

      if (!surname.value.trim()) {
        valid = false;
        message += 'Surname is required.\n';
      }

      if (!valid) {
        alert(message);
        e.preventDefault();
      }
    });
  }
});
