// Automatically fade out alerts after 4 seconds - KR 28/05/2025
setTimeout(function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    });
}, 3000);

document.querySelector('form').addEventListener('submit', function (e) {
  const startTime = document.querySelector('select[name="start_time"]').value;
  const finishTime = document.querySelector('select[name="finish_time"]').value;
  const date = document.querySelector('input[name="date"]').value;

  if (!date) {
    alert("Please select a date.");
    e.preventDefault();
    return;
  }

  if (finishTime <= startTime) {
    alert("Finish time must be after start time.");
    e.preventDefault();
    return;
  }
});