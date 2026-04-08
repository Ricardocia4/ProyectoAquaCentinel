
// Navbar scroll effect
$(window).scroll(function() {
    if ($(window).scrollTop() > 50) {
        $('.navbar').addClass('scrolled');
    } else {
        $('.navbar').removeClass('scrolled');
    }
});

// Smooth scrolling for anchor links
$('a[href*="#"]').on('click', function(e) {
    e.preventDefault();

    $('html, body').animate(
        {
            scrollTop: $($(this).attr('href')).offset().top - 70,
        },
        500,
        'linear'
    );
});

// Animación de elementos al hacer scroll
function checkScroll() {
    const elements = document.querySelectorAll('.fade-in');

    elements.forEach(element => {
    const elementTop = element.getBoundingClientRect().top;
    const elementVisible = 150;

    if (elementTop < window.innerHeight - elementVisible) {
        element.classList.add('active');
    }
    });
}

window.addEventListener('scroll', checkScroll);
// Ejecutar una vez al cargar la página
checkScroll();
