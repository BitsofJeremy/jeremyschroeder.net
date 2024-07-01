document.addEventListener('DOMContentLoaded', function() {
    // Hamburger menu functionality
    const hamburger = document.querySelector('.hamburger');
    const navUl = document.querySelector('.navbar ul');

    hamburger.addEventListener('click', function() {
        navUl.classList.toggle('show');
    });

    // Navbar background on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Background image rotation
    const bg = document.getElementById('bg');
    let currentIndex = 0;

    function rotateBackground() {
        const bgDivs = bg.querySelectorAll('div');
        bgDivs[currentIndex].classList.remove('visible', 'top');
        currentIndex = (currentIndex + 1) % bgDivs.length;
        bgDivs[currentIndex].classList.add('visible', 'top');
    }

    // Initialize background
    const bgDivs = bgSettings.images.map(([url, position]) => {
        const div = document.createElement('div');
        div.style.backgroundImage = `url('${url}')`;
        div.style.backgroundPosition = position;
        bg.appendChild(div);
        return div;
    });

    bgDivs[0].classList.add('visible', 'top');
    setInterval(rotateBackground, bgSettings.delay);

    // Contact form submission
    const contactForm = document.getElementById('contact-form');
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(contactForm);

        fetch(contactForm.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                showFlashMessage('Thank you for your message! We\'ll get back to you soon.', 'success');
                contactForm.reset();
            } else {
                showFlashMessage('An error occurred while sending your message. Please try again later.', 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showFlashMessage('An error occurred. Please try again later.', 'error');
        });
    });

    // Flash message handling
    function showFlashMessage(message, type) {
        const flashContainer = document.getElementById('flash-messages');
        const flashMessage = document.createElement('div');
        flashMessage.className = `flash-message ${type}`;
        flashMessage.innerHTML = `
            ${message}
            <button class="close-btn">&times;</button>
        `;
        flashContainer.appendChild(flashMessage);

        const closeBtn = flashMessage.querySelector('.close-btn');
        closeBtn.addEventListener('click', function() {
            flashMessage.remove();
        });

        // Automatically remove the message after 5 seconds
        setTimeout(() => {
            flashMessage.remove();
        }, 5000);
    }
});