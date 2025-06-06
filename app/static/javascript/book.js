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
    setTimeout(() => toast.remove(), 500);
  }, 3000);
}

// Booking validation - 06/06/2025
const bookingForm = document.querySelector('form[action$="/booking"]');
if (bookingForm) {
  bookingForm.addEventListener('submit', function (e) {
    const date = bookingForm.querySelector('input[name="date"]');
    const start = bookingForm.querySelector('select[name="start_time"]');
    const finish = bookingForm.querySelector('select[name="finish_time"]');
    const studio = bookingForm.querySelector('select[name="studio"]');
    const notes = bookingForm.querySelector('textarea[name="notes"]');

    let valid = true;
    let message = '';

    // Reset previous errors - kr 06/06/2025
    [date, start, finish, studio].forEach(el => el.classList.remove('is-invalid'));

    if (!date.value) {
      valid = false;
      message += 'Please select a date.\n';
      date.classList.add('is-invalid');
    }

    if (finish.value <= start.value) {
      valid = false;
      message += 'Finish time must be after start time.\n';
      start.classList.add('is-invalid');
      finish.classList.add('is-invalid');
    }

    if (!studio.value) {
      valid = false;
      message += 'Please select a studio.\n';
      studio.classList.add('is-invalid');
    }

    if (notes.value.length > 300) {
      message += 'Note is too long. Consider shortening it.\n';
      notes.classList.add('is-warning');
    }

    if (!valid) {
      showToast(message.trim(), 'danger');
      e.preventDefault();
    }
  });
}