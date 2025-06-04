  document.addEventListener("DOMContentLoaded", function () {
    const startSelect = document.querySelector('select[name="start_time"]');
    const finishSelect = document.querySelector('select[name="finish_time"]');

    for (let hour = 8; hour <= 17; hour++) {
      const option = document.createElement("option");
      option.value = `${String(hour).padStart(2, '0')}:00`;
      option.textContent = `${String(hour).padStart(2, '0')}:00`;
      startSelect.appendChild(option);
    }

    for (let hour = 9; hour <= 18; hour++) {
      const option = document.createElement("option");
      option.value = `${String(hour).padStart(2, '0')}:00`;
      option.textContent = `${String(hour).padStart(2, '0')}:00`;
      finishSelect.appendChild(option);
    }
  });