$(document).ready(function() {
    // Initialize theme
    initializeTheme();
    
    // Dark mode toggle
    $('#themeToggle').on('click', function() {
        toggleTheme();
    });
    
    // Smooth scrolling for anchor links
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if (target.length) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 80
            }, 1000);
        }
    });

    // Add active class to current nav item
    var currentPath = window.location.pathname;
    $('.nav-link').each(function() {
        var linkPath = $(this).attr('href');
        if (linkPath && (currentPath === linkPath || (currentPath === '/' && linkPath.includes('home')))) {
            $(this).addClass('active');
        }
    });

    // Navbar scroll effect
    $(window).scroll(function() {
        if ($(this).scrollTop() > 50) {
            $('.navbar').addClass('scrolled');
        } else {
            $('.navbar').removeClass('scrolled');
        }
    });

    // Add hover effects to buttons
    $('.btn').hover(
        function() {
            $(this).addClass('shadow-lg');
        },
        function() {
            $(this).removeClass('shadow-lg');
        }
    );

    // Social media icon hover effects
    $('.social-icon').hover(
        function() {
            $(this).addClass('animate__animated animate__pulse');
        },
        function() {
            $(this).removeClass('animate__animated animate__pulse');
        }
    );

    // Fade in animation for page content
    $('.page-section, .hero-section').hide().fadeIn(800);

    // Add loading animation
    $(window).on('load', function() {
        $('.loading').fadeOut();
    });

    // Profile image click animation
    $('.profile-image').on('click', function() {
        $(this).addClass('animate__animated animate__rubberBand');
        setTimeout(() => {
            $(this).removeClass('animate__animated animate__rubberBand');
        }, 1000);
    });

    // Navigation button click effects
    $('.nav-btn').on('click', function(e) {
        var $this = $(this);
        $this.addClass('clicked');
        
        setTimeout(function() {
            $this.removeClass('clicked');
        }, 200);
    });

    // Add ripple effect to buttons
    $('.btn').on('click', function(e) {
        var $btn = $(this);
        var $ripple = $('<span class="ripple"></span>');
        
        $btn.append($ripple);
        
        var btnOffset = $btn.offset();
        var rippleX = e.pageX - btnOffset.left;
        var rippleY = e.pageY - btnOffset.top;
        
        $ripple.css({
            left: rippleX,
            top: rippleY
        }).addClass('animate');
        
        setTimeout(function() {
            $ripple.remove();
        }, 600);
    });

    // Console greeting
    console.log('Welcome to Munish Khan\'s Portfolio! 🚀');
    console.log('Built with Flask, jQuery, and Bootstrap');
});

// Theme functions
function initializeTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
}

function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    const themeIcon = $('#themeIcon');
    
    if (theme === 'dark') {
        themeIcon.removeClass('fa-moon').addClass('fa-sun');
    } else {
        themeIcon.removeClass('fa-sun').addClass('fa-moon');
    }
}

// Add CSS for ripple effect
$('<style>')
    .prop('type', 'text/css')
    .html(`
        .btn {
            position: relative;
            overflow: hidden;
        }
        
        .ripple {
            position: absolute;
            border-radius: 50%;
            background-color: rgba(255, 255, 255, 0.5);
            transform: scale(0);
            animation: ripple-animation 0.6s linear;
            pointer-events: none;
        }
        
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
        

        
        .clicked {
            transform: scale(0.95);
        }
    `)
    .appendTo('head');
