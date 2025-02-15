window.addEventListener("DOMContentLoaded", function() {
    const fadeInElements = document.querySelectorAll('.fade-in');
    fadeInElements.forEach((el, index) => {
        setTimeout(() => {
            el.classList.add('fade-in');
        }, index * 300); // Stagger the fade-in animation
    });
});
