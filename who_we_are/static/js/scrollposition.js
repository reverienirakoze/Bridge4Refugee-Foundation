document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section'); // Your page sections
    const navLinks = document.querySelectorAll('nav ul li a');
  
    window.addEventListener('scroll', () => {
      let current = '';
  
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 150; // Adjust based on header height
        if (scrollY >= sectionTop) {
          current = section.getAttribute('id');
        }
      });
  
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
          link.classList.add('active');
        }
      });
    });
  });