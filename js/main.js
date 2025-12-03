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

    // --- New Form Handlers ---

    window.handleVolunteerSubmit = function (event, serviceName) {
        event.preventDefault();
        const form = event.target;
        const btn = form.querySelector('button');

        const name = form.querySelector('input[type="text"]').value;
        const phone = form.querySelector('input[type="tel"]').value;
        const service = form.querySelector('select').value;

        btn.innerText = 'Registering...';
        btn.disabled = true;

        setTimeout(async () => {
            if (window.db) {
                await window.db.saveVolunteer({ name, phone, service });
                alert('Registration Successful! We will contact you soon.');
                form.reset();
                closeModal();
            }
            btn.innerText = 'Register';
            btn.disabled = false;
        }, 1000);
    };

    window.handleBookingSubmit = function (event, type) {
        event.preventDefault();
        const form = event.target;
        const btn = form.querySelector('button');

        // Handle different form structures
        const name = form.querySelector('input[type="text"]').value;
        // Some forms might have amount, others date. 
        // For Pooja/Seva, we treat it as a booking request.
        // If it involves payment, we might want to redirect to payment page, 
        // but for now, let's store it as a booking/inquiry.

        let date = new Date().toISOString().split('T')[0];
        const dateInput = form.querySelector('input[type="date"]');
        if (dateInput) date = dateInput.value;

        btn.innerText = 'Processing...';
        btn.disabled = true;

        setTimeout(async () => {
            if (window.db) {
                await window.db.saveBooking({ name, type, date });
                alert('Request Received! We will contact you for confirmation.');
                form.reset();
                closeModal();
            }
            btn.innerText = 'Book Now'; // Or Donate/Sponsor
            btn.disabled = false;
        }, 1000);
    };
    // Load Recent Donors (Public Display)
    async function loadRecentDonors() {
        const container = document.getElementById('recent-donors-list');
        if (!container) return;

        if (window.db) {
            try {
                const donations = await window.db.getDonations();
                // Show last 6 donations
                const recent = donations.slice(0, 6);

                if (recent.length === 0) {
                    container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; color: #94a3b8;">Be the first to donate!</div>';
                    return;
                }

                container.innerHTML = recent.map(d => `
                    <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;">
                        <div style="font-weight: 600; color: #1e293b; font-size: 1.1rem; margin-bottom: 5px;">${d.donor_name || d.donorName || 'Anonymous'}</div>
                        <div style="font-size: 0.9rem; color: #64748b; margin-bottom: 10px;">${d.purpose || 'General Donation'}</div>
                        <div style="font-weight: 700; color: var(--primary-color);">₹${d.amount}</div>
                    </div>
                `).join('');
            } catch (e) {
                console.error('Error loading donors:', e);
                container.innerHTML = '<div style="text-align: center; color: #ef4444;">Unable to load donors.</div>';
            }
        }
    }

    // Call it on load
    loadRecentDonors();

    // --- User Session Management ---
    function checkUserSession() {
        const user = JSON.parse(localStorage.getItem('user'));
        const navLinks = document.querySelector('.nav-links');

        if (navLinks) {
            // Remove existing auth links to prevent duplicates
            const existingAuth = navLinks.querySelector('.auth-link');
            if (existingAuth) existingAuth.remove();

            const li = document.createElement('li');
            li.className = 'auth-link';

            if (user) {
                li.innerHTML = `<a href="profile.html" style="color: var(--primary-color); font-weight: bold;"><i class="fas fa-user-circle"></i> ${user.name.split(' ')[0]}</a>`;
            } else {
                li.innerHTML = `<a href="login.html"><i class="fas fa-sign-in-alt"></i> Login</a>`;
            }
            navLinks.appendChild(li);
        }
    }
    checkUserSession();

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
