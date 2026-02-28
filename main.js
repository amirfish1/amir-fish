/* ============================================
   AmirFish.com — Main JavaScript
   ============================================ */

// ---- Navigation ----
document.addEventListener('DOMContentLoaded', () => {
    const nav = document.getElementById('nav');
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    // Scroll behavior
    const handleScroll = () => {
        if (window.scrollY > 60) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    // Mobile toggle
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
        });

        // Close on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('open');
            });
        });
    }

    // ---- Scroll Animations ----
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -60px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.problem-card, .service-card, .pricing-card, .approach-step, .case-card-full').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
        observer.observe(el);
    });

    // Add staggered delay
    document.querySelectorAll('.problems-grid .problem-card, .services-grid .service-card, .pricing-grid .pricing-card').forEach((el, i) => {
        el.style.transitionDelay = `${i * 0.1}s`;
    });

    // Visible class handler
    const style = document.createElement('style');
    style.textContent = '.visible { opacity: 1 !important; transform: translateY(0) !important; }';
    document.head.appendChild(style);

    // ---- Maturity Journey Animation ----
    const maturityDots = document.querySelectorAll('.maturity-dot');
    if (maturityDots.length > 0) {
        let activeIndex = 0;
        setInterval(() => {
            maturityDots.forEach(dot => dot.classList.remove('active'));
            activeIndex = (activeIndex + 1) % maturityDots.length;
            maturityDots[activeIndex].classList.add('active');
        }, 2500);
    }
});


/* ============================================
   Stripe Payment Integration
   ============================================ 
   
   HOW TO SET UP STRIPE:
   
   1. Create a Stripe account at https://stripe.com
   2. In Stripe Dashboard, create Products with Prices:
      - "AI Quick Win Session" — $200 one-time
      - "AI Roadmap Sprint" — $1,000 one-time
      - "Build & Launch" — $2,000 one-time (or $4,000)
      - "Monthly AI Retainer" — $800/month recurring
   3. Replace the STRIPE_CONFIG values below with your real keys
   4. Create a Stripe Checkout session via your backend (see below)
   
   OPTION A: Stripe Payment Links (EASIEST — No backend needed)
   ─────────────────────────────────────────────────────────────
   Go to Stripe Dashboard → Payment Links → Create for each product.
   Then just replace the button hrefs with those payment link URLs.
   
   OPTION B: Stripe Checkout (More control — Needs backend)
   ─────────────────────────────────────────────────────────────
   Use the code below with a simple backend (Node/Python/etc.)
   
   ============================================ */

const STRIPE_CONFIG = {
    // Replace with your Stripe publishable key
    publishableKey: 'pk_test_REPLACE_WITH_YOUR_KEY',
    
    // Replace with your Stripe Payment Link URLs (Option A - easiest)
    // Create these at: https://dashboard.stripe.com/payment-links
    paymentLinks: {
        quickWin: '#',      // Replace: https://buy.stripe.com/your_quick_win_link
        roadmap: '#',       // Replace: https://buy.stripe.com/your_roadmap_link
        buildLaunch: '#',   // Replace: https://buy.stripe.com/your_build_launch_link
        retainer: '#'       // Replace: https://buy.stripe.com/your_retainer_link
    },

    // For Option B (Stripe Checkout with backend):
    // Replace with your Stripe Price IDs from the Dashboard
    priceIds: {
        quickWin: 'price_REPLACE_ME',
        roadmap: 'price_REPLACE_ME',
        buildLaunch: 'price_REPLACE_ME',
        retainer: 'price_REPLACE_ME'
    }
};

// ---- Payment Handler ----

function handlePayment(packageType) {
    // Option A: Redirect to Stripe Payment Link (recommended to start)
    const link = STRIPE_CONFIG.paymentLinks[packageType];
    
    if (link && link !== '#') {
        window.location.href = link;
        return;
    }

    // Option B: Stripe Checkout (requires backend)
    // Uncomment and implement when you have a backend:
    /*
    const stripe = Stripe(STRIPE_CONFIG.publishableKey);
    
    fetch('/api/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            priceId: STRIPE_CONFIG.priceIds[packageType],
            successUrl: window.location.origin + '/packages.html?success=true',
            cancelUrl: window.location.origin + '/packages.html?canceled=true'
        })
    })
    .then(res => res.json())
    .then(data => stripe.redirectToCheckout({ sessionId: data.sessionId }))
    .catch(err => {
        console.error('Payment error:', err);
        alert('Something went wrong. Please try again or email amir@amirfish.com');
    });
    */

    // Fallback: show setup instructions
    alert(
        'Payment links not configured yet.\n\n' +
        'To set up payments:\n' +
        '1. Create a Stripe account\n' +
        '2. Create Payment Links for each package\n' +
        '3. Add the URLs to STRIPE_CONFIG in main.js\n\n' +
        'See the comments in main.js for full instructions.'
    );
}

// ---- Success / Cancel URL Handling ----
(function checkPaymentStatus() {
    const params = new URLSearchParams(window.location.search);
    
    if (params.get('success') === 'true') {
        // Show success message
        const banner = document.createElement('div');
        banner.style.cssText = `
            position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
            background: #059669; color: white; text-align: center;
            padding: 16px; font-family: 'DM Sans', sans-serif; font-weight: 600;
            animation: slideDown 0.5s ease-out;
        `;
        banner.innerHTML = `
            ✓ Payment received! Check your email for booking details. 
            <a href="index.html" style="color: white; text-decoration: underline; margin-left: 12px;">Back to Home</a>
        `;
        document.body.prepend(banner);
        
        // Clean URL
        window.history.replaceState({}, '', window.location.pathname);
    }
    
    if (params.get('canceled') === 'true') {
        window.history.replaceState({}, '', window.location.pathname);
    }
})();
