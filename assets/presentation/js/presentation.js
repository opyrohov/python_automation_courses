/**
 * Python Automation Course - Global Presentation Navigation Script
 * This script is shared across all lecture presentations
 * Handles slide navigation, keyboard shortcuts, and UI updates
 */

let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
let isTransitioning = false;

// Initialize slide counter
document.getElementById('totalSlides').textContent = totalSlides;

/**
 * Display the slide at the specified index
 * @param {number} n - The index of the slide to show
 */
function showSlide(n) {
    // Prevent rapid transitions
    if (isTransitioning) {
        return;
    }

    // Store the old slide index
    const oldSlide = currentSlide;

    // Validate slide index FIRST
    if (n >= totalSlides) {
        currentSlide = totalSlides - 1;
    } else if (n < 0) {
        currentSlide = 0;
    } else {
        currentSlide = n;
    }

    // If we're already on this slide, do nothing
    if (oldSlide === currentSlide) {
        return;
    }

    // Set transitioning flag
    isTransitioning = true;

    // Remove active class from old slide
    slides[oldSlide].classList.remove('active');

    // Add active class to new slide
    slides[currentSlide].classList.add('active');

    // Update slide counter
    document.getElementById('currentSlide').textContent = currentSlide + 1;

    // Update button states
    document.getElementById('prevBtn').disabled = currentSlide === 0;
    document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;

    // Scroll to top of slide
    slides[currentSlide].scrollTop = 0;

    // Update scroll indicator for the new slide
    setTimeout(() => {
        updateAllScrollIndicators();
    }, 50);

    // Clear transitioning flag after animation completes (300ms transition)
    setTimeout(() => {
        isTransitioning = false;
    }, 350);
}

/**
 * Change slide by the specified direction
 * @param {number} direction - Number of slides to move (positive or negative)
 */
function changeSlide(direction) {
    showSlide(currentSlide + direction);
}

/**
 * Go to first slide
 */
function goToFirstSlide() {
    showSlide(0);
}

/**
 * Go to last slide
 */
function goToLastSlide() {
    showSlide(totalSlides - 1);
}

/**
 * Go to next slide
 */
function nextSlide() {
    changeSlide(1);
}

/**
 * Go to previous slide
 */
function previousSlide() {
    changeSlide(-1);
}

// Keyboard navigation
document.addEventListener('keydown', function(event) {
    switch(event.key) {
        case 'ArrowRight':
        case 'PageDown':
            changeSlide(1);
            break;
        case 'ArrowLeft':
        case 'PageUp':
            changeSlide(-1);
            break;
        case 'Home':
            goToFirstSlide();
            break;
        case 'End':
            goToLastSlide();
            break;
        case 'Escape':
            // Could be used to exit fullscreen in the future
            break;
    }
});

// Touch/Swipe support for mobile devices
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', function(event) {
    touchStartX = event.changedTouches[0].screenX;
}, false);

document.addEventListener('touchend', function(event) {
    touchEndX = event.changedTouches[0].screenX;
    handleSwipe();
}, false);

function handleSwipe() {
    const swipeThreshold = 50; // Minimum distance for a swipe

    if (touchEndX < touchStartX - swipeThreshold) {
        // Swiped left - go to next slide
        changeSlide(1);
    }

    if (touchEndX > touchStartX + swipeThreshold) {
        // Swiped right - go to previous slide
        changeSlide(-1);
    }
}

/**
 * Add scroll indicators to all slides
 */
function addScrollIndicators() {
    slides.forEach(slide => {
        const indicator = document.createElement('div');
        indicator.className = 'scroll-indicator';

        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('div');
            dot.className = 'dot';
            indicator.appendChild(dot);
        }

        slide.appendChild(indicator);
    });
}

/**
 * Update scroll indicator visibility for a specific slide
 * @param {HTMLElement} slide - The slide element to check
 */
function updateScrollIndicator(slide) {
    const indicator = slide.querySelector('.scroll-indicator');
    if (!indicator) return;

    // Check if content is scrollable
    const isScrollable = slide.scrollHeight > slide.clientHeight;

    // Check if scrolled to bottom (with 5px tolerance)
    const isAtBottom = slide.scrollTop + slide.clientHeight >= slide.scrollHeight - 5;

    // Show indicator if scrollable and not at bottom
    if (isScrollable && !isAtBottom) {
        indicator.classList.add('visible');
    } else {
        indicator.classList.remove('visible');
    }
}

/**
 * Update all scroll indicators
 */
function updateAllScrollIndicators() {
    const activeSlide = document.querySelector('.slide.active');
    if (activeSlide) {
        updateScrollIndicator(activeSlide);
    }
}

// Add scroll event listeners to all slides
function initScrollIndicators() {
    slides.forEach(slide => {
        slide.addEventListener('scroll', () => {
            if (slide.classList.contains('active')) {
                updateScrollIndicator(slide);
            }
        });
    });
}

// Initialize presentation
addScrollIndicators();
initScrollIndicators();
showSlide(0);

// Update indicator after a short delay to ensure layout is complete
setTimeout(updateAllScrollIndicators, 100);

// Update indicators on window resize
window.addEventListener('resize', updateAllScrollIndicators);

// Log presentation info to console
console.log(`Presentation loaded: ${totalSlides} slides`);
console.log('Keyboard shortcuts:');
console.log('  → or PageDown: Next slide');
console.log('  ← or PageUp: Previous slide');
console.log('  Home: First slide');
console.log('  End: Last slide');
