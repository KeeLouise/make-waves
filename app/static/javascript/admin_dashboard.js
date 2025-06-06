document.addEventListener('DOMContentLoaded', function () {
  
  document.querySelectorAll('[data-toast]').forEach(el => {
    const message = el.getAttribute('data-toast');
    const type = el.getAttribute('data-toast-type') || 'success';
    showToast(message, type);
  });

  setTimeout(() => {
    document.querySelectorAll('.alert').forEach(alert => {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    });
  }, 3000);
});

function showToast(message, type = 'success') {
  const toast = document.createElement('div');
  toast.className = `toast-notification toast-${type}`;
  toast.textContent = message;

  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => {
      if (toast.parentNode) toast.remove();
    }, 500);
  }, 3000);
}