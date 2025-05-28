// Automatically fade out alerts after 4 seconds - KR 28/05/2025
setTimeout(function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    });
}, 3000);