// Netflix Theme Portfolio - Anuj DM
// Cinematic Effects

// ==================== CINEMATIC LOADER ====================
window.addEventListener('load', function() {
    setTimeout(() => {
        document.getElementById('loader').classList.add('hidden');
    }, 2000);
});

// ==================== SCROLL TIMELINE ====================
window.addEventListener('scroll', function() {
    const scrollProgress = document.getElementById('scrollProgress');
    const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (window.scrollY / windowHeight);
    scrollProgress.style.transform = `scaleX(${scrolled})`;
});

// ==================== PARALLAX DEPTH LAYERS ====================
const hero = document.querySelector('.hero');
if (hero) {
    document.addEventListener('mousemove', (e) => {
        const layers = document.querySelectorAll('.parallax-layer');
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        
        layers.forEach((layer, index) => {
            const speed = (index + 1) * 10;
            const xPos = (x - 0.5) * speed;
            const yPos = (y - 0.5) * speed;
            layer.style.transform = `translate(${xPos}px, ${yPos}px)`;
        });
    });
}

// Certificate images array
const certImages = [
    'images/1-800549af-7f01-4298-87d3-6cfd0c6c1317.jpg',
    'images/anuj-dm-3d51f6b2-e61c-4915-b4f9-0e24c8084e2e-certificate.jpg',
    'images/anuj-dm-a8cb24fd-8176-4af7-bf3b-77c715354000-certificate (1).jpg',
    'images/UC-1d1902c0-cde0-48bf-9a6c-017805e86f05 (1).jpg',
    'images/UC-4d5040f7-2673-4808-a48b-7dd9c909a8fd (1).jpg',
    'images/ANUJ+D+M_152118534-images-0.jpg'
];

// Open Certificate Modal
function openModal(index) {
    const modal = document.getElementById('certModal');
    const modalImg = document.getElementById('modalImage');
    
    modal.classList.add('show');
    modalImg.src = certImages[index];
    document.body.style.overflow = 'hidden';
}

// Close Certificate Modal
function closeModal() {
    const modal = document.getElementById('certModal');
    modal.classList.remove('show');
    document.body.style.overflow = 'auto';
}

// Close modal on ESC key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
        closeSuccess();
    }
});

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Contact Form
document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    
    // Disable submit button
    const submitBtn = this.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending...';
    
    try {
        const response = await fetch('/api/contact', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name, email, message })
});

        
        const data = await response.json();
        
        if (response.ok) {
            // Show success modal
            document.getElementById('successModal').classList.add('show');
            
            // Clear form
            this.reset();
        } else {
            alert('Error: ' + (data.error || 'Failed to send message'));
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to send message. Make sure the server is running!');
    } finally {
        // Re-enable submit button
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    }
});

// Close success modal
function closeSuccess() {
    document.getElementById('successModal').classList.remove('show');
}

// Smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Console message
console.log('%c🎬 ANUJ DM - Filmmaker Portfolio', 'font-size: 20px; font-weight: bold; color: #E50914;');
console.log('%cNetflix Theme | Crafted with ❤️', 'color: #808080;');
