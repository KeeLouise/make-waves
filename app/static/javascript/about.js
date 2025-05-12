//Gallery script
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.gallery-image');
    const prev = document.getElementById('prev');
    const next = document.getElementById('next');
    let index = 0;
    let autoplayInterval;
  
    function updateGallery() {
      images.forEach((img, i) => {
        img.classList.toggle('active', i === index);
      });
    }
  
    function showNext() {
      index = (index + 1) % images.length;
      updateGallery();
    }
  
    function showPrev() {
      index = (index - 1 + images.length) % images.length;
      updateGallery();
    }
  
    prev.addEventListener('click', () => {
      showPrev();
      resetAutoplay();
    });
  
    next.addEventListener('click', () => {
      showNext();
      resetAutoplay();
    });
  
    function startAutoplay() {
      autoplayInterval = setInterval(showNext, 3000);
    }
  
    function resetAutoplay() {
      clearInterval(autoplayInterval);
      startAutoplay();
    }
  
    updateGallery();
    startAutoplay();
  });