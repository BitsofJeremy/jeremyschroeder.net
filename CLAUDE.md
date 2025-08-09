# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal portfolio website (jeremyschroeder.net) built with Flask. The site features a minimalist design with a video background and glassmorphism UI elements.

## Architecture

- **Framework**: Flask web application (Python 3.10+)
- **Structure**: Simple single-page application with template inheritance
- **Templates**: Jinja2 templates using Bootstrap 5 and Font Awesome
- **Static Assets**: Profile image, favicon, and background video stored in `/static`
- **Logging**: Rotating file handler for production logs in `/logs` directory

### Key Files

- `app.py`: Main Flask application with configuration and single route
- `templates/base.html`: Base template with video background and glassmorphism styling
- `templates/index.html`: Homepage content extending base template
- `pyproject.toml`: Python project configuration and dependencies

## Development Commands

### Running the Application
```bash
# Development mode
python app.py

# Production mode  
FLASK_ENV=production python app.py
```

### Environment Variables
- `FLASK_ENV`: Set to 'development' for debug mode
- `FLASK_DEBUG`: Set to 'true' to enable debug mode
- `SECRET_KEY`: Flask secret key (auto-generated if not set)
- `CSRF_SESSION_KEY`: CSRF protection key (auto-generated if not set)

### Dependencies
Install dependencies using uv (lock file present) or pip:
```bash
# With uv
uv sync

# With pip
pip install -r requirements.txt
```

## Design System

The site uses a dark theme with glassmorphism effects:
- Font: B612 Mono (Google Fonts)
- Background: Video with fallback gradient for Safari
- UI: Glass containers with backdrop blur
- Colors: White text on dark/transparent backgrounds
- Layout: Centered single-column design with fixed footer

## Configuration Notes

- Default server runs on 127.0.0.1:5052
- Security features enabled: CSRF protection, secure cookies
- Session timeout: 4 hours
- Logging: Rotating file handler (10MB max, 10 backups)