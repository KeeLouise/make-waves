// Automatically fade out Bootstrap alerts after 3 seconds – KR 22/05/2025
setTimeout(function () {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    const bsAlert = new bootstrap.Alert(alert);
    bsAlert.close();
  });
}, 3000);

// Toast notification logic – KR 05/06/2025
function showToast(message, type = 'success') {
  const toast = document.createElement('div');
  toast.className = `toast-notification toast-${type}`;
  toast.textContent = message;

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 500);
  }, 3000);
}

// Trigger toast from hidden elements – KR 05/06/2025
document.querySelectorAll('[data-toast]').forEach(el => {
  const message = el.getAttribute('data-toast');
  const type = el.getAttribute('data-toast-type') || 'success';
  showToast(message, type);
});

// Registration form validation – KR 30/05/2025
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
        showToast(message, 'danger');
        e.preventDefault();
      }
    });
  }
});
