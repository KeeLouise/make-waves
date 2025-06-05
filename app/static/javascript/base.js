document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.getElementById('hamburger');
    const mobileNav = document.getElementById('mobile-nav');

    hamburger.addEventListener('click', function () {
      mobileNav.classList.toggle('active');
      hamburger.classList.toggle('open');
    });
  });
  document.querySelectorAll('#mobile-nav a').forEach(link => {
  link.addEventListener('click', () => {
    mobileNav.classList.remove('active');
    hamburger.classList.remove('open');
  });
});