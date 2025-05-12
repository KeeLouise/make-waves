document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.gallery-image');
    const prevBtn = document.getElementById('prev');
    const nextBtn = document.getElementById('next');
    let current = 0;
  
    function updateGallery() {
      images.forEach((img, i) => {
        img.classList.toggle('active', i === current);
      });
    }
  
    prevBtn.addEventListener('click', () => {
      current = (current - 1 + images.length) % images.length;
      updateGallery();
    });
  
    nextBtn.addEventListener('click', () => {
      current = (current + 1) % images.length;
      updateGallery();
    });
  
    updateGallery(); // initialize
  });