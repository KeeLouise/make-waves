document.addEventListener('DOMContentLoaded', function () {
  // Toast logic
  document.querySelectorAll('[data-toast]').forEach(el => {
    const message = el.getAttribute('data-toast');
    const type = el.getAttribute('data-toast-type') || 'success';
    showToast(message, type);
  });
});

function showToast(message, type = 'success') {
  const toast = document.createElement('div');
  toast.className = `toast-notification toast-${type}`;
  toast.textContent = message;

  Object.assign(toast.style, {
    position: 'fixed',
    top: '1rem',
    right: '1rem',
    zIndex: '1055',
    padding: '1rem',
    backgroundColor: type === 'danger' ? '#dc3545' : '#28a745',
    color: '#fff',
    borderRadius: '5px',
    boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
    transition: 'opacity 0.5s ease',
    opacity: '1',
  });

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => {
      if (toast.parentNode) toast.remove();
    }, 500);
  }, 3000);
}

  // Registration form validation – KR 30/05/2025
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

  // Login validation – KR 06/06/2025
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