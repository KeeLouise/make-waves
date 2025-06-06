document.addEventListener('DOMContentLoaded', function () {
  const toastDataContainer = document.getElementById('toast-data-container');
  if (toastDataContainer) {
    toastDataContainer.querySelectorAll('[data-toast]').forEach(el => {
      const message = el.getAttribute('data-toast');
      const type = el.getAttribute('data-toast-type') || 'success';
      showToast(message, type);
    });
    toastDataContainer.remove(); // Prevent duplicate display
  }

  // Registration form validation - KR 06/06/2025
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

  // Login form validation - KR 06/06/2025
  const loginForm = document.querySelector('#login-card form');
  if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
      const email = loginForm.querySelector('#email');
      const password = loginForm.querySelector('#password');

      let valid = true;
      let message = '';

      if (!email.value.includes('@')) {
        valid = false;
        message += 'Invalid email format.\n';
      }

      if (!password.value.trim()) {
        valid = false;
        message += 'Password is required.\n';
      }

      if (!valid) {
        showToast(message, 'danger');
        e.preventDefault();
      }
    });
  }

  // Edit profile form validation - KR 06/06/2025
  const editProfileForm = document.querySelector('form[action$="/edit-profile"]');
  if (editProfileForm) {
    editProfileForm.addEventListener('submit', function (e) {
      const username = editProfileForm.querySelector('#username');
      const email = editProfileForm.querySelector('#email');
      const firstName = editProfileForm.querySelector('#first_name');
      const surname = editProfileForm.querySelector('#surname');

      let valid = true;
      let message = '';

      if (!username.value.trim()) {
        valid = false;
        message += 'Username is required.\n';
      }

      if (!email.value.includes('@')) {
        valid = false;
        message += 'Invalid email format.\n';
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

function showToast(message, type = 'success') {
  let container = document.getElementById('toast-container');
  
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.style.position = 'fixed';
    container.style.top = '1rem';
    container.style.right = '1rem';
    container.style.zIndex = '9999';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast-notification toast-${type}`;
  toast.textContent = message;
  toast.style.opacity = '1';

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 500);
  }, 3000);
}