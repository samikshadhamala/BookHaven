/**
 * JavaScript for BookHaven Online Bookstore
 * Handles form validation, animations, and interactivity
 * Web Technology (BIT233) Assignment
 */

$(document).ready(function() {
    // ============= FORM VALIDATION =============
    
    // Registration Form Validation
    $('#registerForm').on('submit', function(e) {
        let isValid = true;
        
        // Username validation (minimum 3 characters)
        const username = $('input[name="username"]').val();
        if (username.length < 3) {
            showError('username', 'Username must be at least 3 characters');
            isValid = false;
        }
        
        // Email validation
        const email = $('input[name="email"]').val();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showError('email', 'Please enter a valid email address');
            isValid = false;
        }
        
        // Password validation (minimum 8 characters)
        const password = $('input[name="password"]').val();
        if (password.length < 8) {
            showError('password', 'Password must be at least 8 characters');
            isValid = false;
        }
        
        // Confirm password validation
        const confirmPassword = $('input[name="confirm_password"]').val();
        if (password !== confirmPassword) {
            showError('confirm_password', 'Passwords do not match');
            isValid = false;
        }
        
        if (!isValid) {
            e.preventDefault();
        }
    });
    
    // Helper function to show error messages
    function showError(fieldName, message) {
        const field = $(`input[name="${fieldName}"]`);
        field.addClass('is-invalid');
        
        // Remove existing error message
        field.siblings('.invalid-feedback').remove();
        
        // Add new error message
        field.after(`<div class="invalid-feedback d-block">${message}</div>`);
    }
    
    // Clear error on input
    $('input').on('input', function() {
        $(this).removeClass('is-invalid');
        $(this).siblings('.invalid-feedback').remove();
    });
    
    // ============= SMOOTH SCROLLING =============
    $('a[href^="#"]').on('click', function(e) {
        e.preventDefault();
        const target = $(this.getAttribute('href'));
        if (target.length) {
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 80
            }, 800);
        }
    });
    
    // ============= ANIMATIONS ON SCROLL =============
    const animateOnScroll = () => {
        $('.animate-fade-in, .animate-slide-up').each(function() {
            const elementTop = $(this).offset().top;
            const elementBottom = elementTop + $(this).outerHeight();
            const viewportTop = $(window).scrollTop();
            const viewportBottom = viewportTop + $(window).height();
            
            if (elementBottom > viewportTop && elementTop < viewportBottom) {
                $(this).css('opacity', '1');
                $(this).css('transform', 'translateY(0)');
            }
        });
    };
    
    // Initialize animations
    $('.animate-fade-in').css({ 'opacity': '0', 'transition': 'opacity 0.6s ease-in' });
    $('.animate-slide-up').css({ 
        'opacity': '0', 
        'transform': 'translateY(30px)', 
        'transition': 'all 0.6s ease-out' 
    });
    
    $(window).on('scroll', animateOnScroll);
    animateOnScroll(); // Run on page load
    
    // ============= CART QUANTITY VALIDATION =============
    $('.add-to-cart-form input[type="number"]').on('change', function() {
        const max = parseInt($(this).attr('max'));
        const min = parseInt($(this).attr('min'));
        let value = parseInt($(this).val());
        
        if (value > max) {
            $(this).val(max);
            alert(`Maximum ${max} items available in stock`);
        } else if (value < min) {
            $(this).val(min);
        }
    });
    
    // ============= SEARCH FUNCTIONALITY =============
    $('#searchInput').on('input', function() {
        const searchTerm = $(this).val().toLowerCase();
        
        $('.book-card').each(function() {
            const bookTitle = $(this).find('.book-title').text().toLowerCase();
            const bookAuthor = $(this).find('.book-author').text().toLowerCase();
            
            if (bookTitle.includes(searchTerm) || bookAuthor.includes(searchTerm)) {
                $(this).parent().show();
            } else {
                $(this).parent().hide();
            }
        });
    });
    
    // ============= ALERT AUTO DISMISS =============
    setTimeout(function() {
        $('.alert').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 5000);
    
    // ============= LOADING SPINNER FOR FORMS =============
    $('form').on('submit', function() {
        const submitBtn = $(this).find('button[type="submit"]');
        const originalText = submitBtn.html();
        
        submitBtn.prop('disabled', true);
        submitBtn.html('<i class="fas fa-spinner fa-spin"></i> Processing...');
        
        // Re-enable after 3 seconds (fallback)
        setTimeout(function() {
            submitBtn.prop('disabled', false);
            submitBtn.html(originalText);
        }, 3000);
    });
    
    // ============= CONFIRM DELETE ACTIONS =============
    $('.delete-btn').on('click', function(e) {
        if (!confirm('Are you sure you want to delete this item?')) {
            e.preventDefault();
        }
    });
    
    // ============= NAVBAR SCROLL EFFECT =============
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 50) {
            $('.navbar').css('background', 'linear-gradient(135deg, #654321 0%, #3d2817 100%)');
        } else {
            $('.navbar').css('background', 'linear-gradient(135deg, #8B4513 0%, #654321 100%)');
        }
    });
    
    // ============= BOOK CARD HOVER EFFECTS =============
    $('.book-card').hover(
        function() {
            $(this).find('.btn-view').css('opacity', '1');
        },
        function() {
            $(this).find('.btn-view').css('opacity', '0.9');
        }
    );
    
    // ============= NUMBER INPUT INCREMENT/DECREMENT =============
    $('.quantity-input').each(function() {
        const input = $(this);
        const btnDecrease = $('<button type="button" class="btn btn-sm btn-outline-secondary">-</button>');
        const btnIncrease = $('<button type="button" class="btn btn-sm btn-outline-secondary">+</button>');
        
        input.wrap('<div class="input-group input-group-sm"></div>');
        input.before(btnDecrease);
        input.after(btnIncrease);
        
        btnDecrease.on('click', function() {
            const currentVal = parseInt(input.val()) || 0;
            const minVal = parseInt(input.attr('min')) || 1;
            if (currentVal > minVal) {
                input.val(currentVal - 1);
                input.trigger('change');
            }
        });
        
        btnIncrease.on('click', function() {
            const currentVal = parseInt(input.val()) || 0;
            const maxVal = parseInt(input.attr('max')) || 999;
            if (currentVal < maxVal) {
                input.val(currentVal + 1);
                input.trigger('change');
            }
        });
    });
    
    // ============= PRICE FORMATTING =============
    $('.book-price').each(function() {
        const price = $(this).text().replace('NPR', '').trim();
        const formattedPrice = parseFloat(price).toFixed(2);
        $(this).text(`NPR ${formattedPrice}`);
    });
    
    // ============= CATEGORY FILTER =============
    $('.category-filter').on('change', function() {
        const selectedCategory = $(this).val();
        
        if (selectedCategory === '') {
            $('.book-card').parent().show();
        } else {
            $('.book-card').parent().hide();
            $(`.book-card[data-category="${selectedCategory}"]`).parent().show();
        }
    });
    
    // ============= RATING STARS =============
    $('.rating-stars').each(function() {
        const rating = parseFloat($(this).data('rating'));
        const stars = $(this);
        stars.empty();
        
        for (let i = 1; i <= 5; i++) {
            if (i <= Math.floor(rating)) {
                stars.append('<i class="fas fa-star"></i>');
            } else if (i === Math.ceil(rating) && rating % 1 !== 0) {
                stars.append('<i class="fas fa-star-half-alt"></i>');
            } else {
                stars.append('<i class="far fa-star"></i>');
            }
        }
    });
    
    // ============= TOOLTIP INITIALIZATION =============
    $('[data-bs-toggle="tooltip"]').tooltip();
    
    // ============= IMAGE LAZY LOADING =============
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('img[loading="lazy"]');
        images.forEach(img => {
            img.src = img.dataset.src;
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
        document.body.appendChild(script);
    }
    
    // ============= COPY TO CLIPBOARD =============
    $('.copy-btn').on('click', function() {
        const textToCopy = $(this).data('copy');
        navigator.clipboard.writeText(textToCopy).then(function() {
            alert('Copied to clipboard!');
        });
    });
    
    // ============= PRINT FUNCTIONALITY =============
    $('.print-btn').on('click', function() {
        window.print();
    });
    
    console.log('BookHaven JavaScript loaded successfully!');
});

// ============= VANILLA JS FUNCTIONS =============

/**
 * Validate email format
 */
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

/**
 * Format price with currency
 */
function formatPrice(price) {
    return `NPR ${parseFloat(price).toFixed(2)}`;
}

/**
 * Calculate discount percentage
 */
function calculateDiscount(originalPrice, discountedPrice) {
    return Math.round(((originalPrice - discountedPrice) / originalPrice) * 100);
}

/**
 * Debounce function for search
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Show loading spinner
 */
function showLoading() {
    document.body.insertAdjacentHTML('beforeend', `
        <div id="loading-overlay" style="
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
        ">
            <div class="spinner-border text-light" role="status" style="width: 3rem; height: 3rem;">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
    `);
}

/**
 * Hide loading spinner
 */
function hideLoading() {
    const overlay = document.getElementById('loading-overlay');
    if (overlay) {
        overlay.remove();
    }
}

/**
 * Show success toast notification
 */
function showToast(message, type = 'success') {
    const toastHtml = `
        <div class="toast-notification ${type}" style="
            position: fixed;
            top: 100px;
            right: 20px;
            background: ${type === 'success' ? '#28a745' : '#dc3545'};
            color: white;
            padding: 1rem 2rem;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            z-index: 9999;
            animation: slideInRight 0.3s ease-out;
        ">
            <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
            ${message}
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', toastHtml);
    
    setTimeout(() => {
        const toast = document.querySelector('.toast-notification');
        if (toast) {
            toast.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => toast.remove(), 300);
        }
    }, 3000);
}

// Add CSS for toast animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
