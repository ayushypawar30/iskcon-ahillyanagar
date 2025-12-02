document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileBtn) {
        mobileBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Smooth Scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Modal Logic
    window.openModal = function (modalId) {
        const modal = document.getElementById(modalId);
        const overlay = document.getElementById('modal-overlay');
        if (modal && overlay) {
            modal.classList.add('active');
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        }
    };

    function closeModal() {
        document.querySelectorAll('.modal').forEach(m => m.classList.remove('active'));
        const overlay = document.getElementById('modal-overlay');
        if (overlay) overlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    // Close modal on overlay click or close button click
    const overlay = document.getElementById('modal-overlay');
    if (overlay) {
        overlay.addEventListener('click', closeModal);
    }

    document.querySelectorAll('.close-modal').forEach(btn => {
        btn.addEventListener('click', closeModal);
    });

    // Close on Escape key
    window.openLightbox = function (src) {
        const lightbox = document.getElementById('lightbox');
        const img = document.getElementById('lightbox-img');
        if (lightbox && img) {
            img.src = src;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    };

    window.closeLightbox = function () {
        const lightbox = document.getElementById('lightbox');
        if (lightbox) {
            lightbox.classList.remove('active');
            document.body.style.overflow = '';
        }
    };

    // --- Payment Redirection Logic ---
    window.initiatePayment = function (event, type) {
        event.preventDefault();
        const form = event.target;
        const name = form.querySelector('input[type="text"]').value;
        const amount = form.querySelector('input[type="number"]').value;

        // Redirect to payment page with params
        window.location.href = `payment.html?amount=${amount}&name=${encodeURIComponent(name)}&type=${encodeURIComponent(type)}`;
    };

    // Alias for compatibility with donation.html
    window.handleFormSubmit = window.initiatePayment;

    // Contact Form Logic
    window.handleContactSubmit = function (event) {
        event.preventDefault();
        const form = event.target;
        const btn = form.querySelector('button[type="submit"]');
        const formContainer = document.getElementById('contact-form-container');
        const thankYouMsg = document.getElementById('thank-you-message');

        // Get values
        const name = form.querySelector('input[type="text"]').value;
        const email = form.querySelector('input[type="email"]').value;
        const message = form.querySelector('textarea').value;

        btn.innerText = 'Sending...';
        btn.disabled = true;

        setTimeout(() => {
            // Save to Database
            if (window.db) {
                window.db.saveContact({
                    name: name,
                    email: email,
                    message: message
                });
            } else {
                console.error('Database not loaded');
            }

            // Show Success Message
            formContainer.style.display = 'none';
            thankYouMsg.style.display = 'block';
            form.reset();
            btn.innerText = 'Send Message';
            btn.disabled = false;
        }, 1500);
    };

    window.resetContactForm = function () {
        document.getElementById('contact-form-container').style.display = 'block';
        document.getElementById('thank-you-message').style.display = 'none';
    };

    // Newsletter Logic
    window.handleSubscriberSubmit = function (event) {
        event.preventDefault();
        const form = event.target;
        const emailInput = form.querySelector('input[type="email"]');
        const btn = form.querySelector('button');
        const email = emailInput.value;

        btn.innerText = '...';
        btn.disabled = true;

        setTimeout(async () => {
            if (window.db) {
                const result = await window.db.saveSubscriber(email);
                if (result && result.status === 'success') {
                    alert('Thank you for subscribing!');
                    form.reset();
                } else {
                    alert('Subscription failed or email already exists.');
                }
            } else {
                console.error('Database not loaded');
            }
            btn.innerText = 'Join';
            btn.disabled = false;
        }, 1000);
    };

    // Scroll Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Select elements to animate
    document.querySelectorAll('.timing-card, .section-title, .hero-content > *, .footer-col').forEach(el => {
        el.classList.add('fade-in-up');
        observer.observe(el);
    });
});
