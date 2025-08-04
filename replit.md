# Overview

This is a personal portfolio website for Munish Khan built using Flask. The application serves as a multilingual (German/English), dark mode-enabled showcase of Munish's professional presence with sections for projects, education, and skills. The site features a modern, responsive design with his professional profile photo, social media integration, and dynamic theme switching functionality.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
The application uses a traditional server-side rendered approach with Flask's templating system. The frontend is built with:
- **Template Engine**: Jinja2 templates with a base template inheritance pattern and multilingual content support
- **CSS Framework**: Bootstrap 5.3.0 for responsive design and UI components
- **Styling**: Custom CSS with CSS variables for dark/light theme support using Inter font family
- **Icons**: Font Awesome 6.4.0 for social media, interface icons, and theme switching
- **JavaScript**: jQuery for DOM manipulation, theme switching, and interactive effects
- **Theme System**: Local storage-based dark/light mode with smooth transitions
- **Internationalization**: Client-side language switching between German and English

The template structure follows a modular approach with `base.html` providing the navigation, theme controls, language switcher, and layout structure, while individual page templates extend this base for consistent styling and navigation.

## Backend Architecture
The backend is implemented as a Flask application with internationalization support:
- **Framework**: Flask with routing for static content delivery and language switching
- **Structure**: Single `app.py` file containing all route definitions and multilingual content
- **Session Management**: Flask sessions for language preference storage with environment-based secret key
- **Internationalization**: Server-side content management with German and English translations
- **Content Management**: Centralized language dictionary with context injection for all templates
- **Logging**: Debug-level logging enabled for development

The application follows a straightforward MVC pattern where Flask handles routing, language switching, and view rendering, templates manage the presentation layer with dynamic content, and static files provide styling and interactivity.

## Deployment Configuration
The application is configured for deployment with:
- **Host Configuration**: Binds to `0.0.0.0` for external access
- **Port**: Uses port 5000
- **Debug Mode**: Enabled for development environments
- **Entry Points**: Both `app.py` and `main.py` can serve as application entry points

# External Dependencies

## CDN Resources
- **Bootstrap CSS**: `cdn.jsdelivr.net/npm/bootstrap@5.3.0` - UI framework
- **Font Awesome**: `cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0` - Icon library
- **Google Fonts**: `fonts.googleapis.com/css2` - Inter font family
- **jQuery**: Implied usage for JavaScript functionality

## Social Media Integration
- **GitHub**: Profile link to `github.com/munishkhan`
- **LinkedIn**: Profile link to `linkedin.com/in/munishkhan`
- **Twitter/X**: Profile link to `x.com/munishkhan`

## Environment Dependencies
- **Flask**: Web framework for Python
- **Environment Variables**: `SESSION_SECRET` for session configuration