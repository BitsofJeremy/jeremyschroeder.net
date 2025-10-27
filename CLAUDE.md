# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a minimalist personal website (jeremyschroeder.net) deployed as a static HTML page on GitHub Pages. The site displays a simple ASCII art logo with a retro terminal aesthetic.

## Architecture

- **Type**: Static HTML website (no backend, no build process)
- **Hosting**: GitHub Pages
- **Structure**: Single HTML file with inline CSS
- **Dependencies**: None - pure HTML/CSS

### Key Files

- `index.html`: Main HTML file containing all markup and styling
- `static/images/favicon.ico`: Site favicon
- `.nojekyll`: GitHub Pages configuration file (prevents Jekyll processing)
- `README.md`: Documentation and deployment instructions
- `CLAUDE.md`: This file

### Archived Files

The following Flask-related files are kept in `archive/` for reference but are no longer used:
- `app.py`: Former Flask application
- `templates/`: Former Jinja2 templates
- `requirements.txt`, `pyproject.toml`, `uv.lock`: Former Python dependencies

## Development

### Local Testing

Simply open the HTML file in a browser, or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using PHP
php -S localhost:8000

# Or just open the file
open index.html
```

### Making Changes

Edit `index.html` directly. The file contains:
- HTML structure
- Inline CSS in the `<head>` section
- ASCII art content in the `<body>`

No build process or compilation required - changes are immediately visible.

## Design System

The site uses a minimalist retro terminal aesthetic:
- **Font**: Courier New (monospace, system font)
- **Background**: Solid black (#000000)
- **Text color**: Terminal green (#00ff00)
- **Effect**: Text glow/shadow for CRT monitor effect
- **Layout**: Centered ASCII art, responsive font sizing

### Responsive Design

- Desktop: 0.7rem font size
- Mobile (<768px): 0.5rem font size

## Deployment

### GitHub Pages Setup

1. Ensure changes are committed to the main branch
2. GitHub Pages should be configured to serve from the root directory
3. The `.nojekyll` file ensures static assets are served correctly
4. Site will be available at your GitHub Pages URL

### Deployment Workflow

```bash
# Make changes to index.html
# Test locally
# Commit and push
git add index.html
git commit -m "Update site content"
git push origin main

# GitHub Pages will auto-deploy within a few minutes
```

## Content Updates

To update the ASCII art or text:
1. Edit the content inside `<div class="ascii-art">` in index.html
2. Maintain the `pre` white-space formatting
3. Test in browser to ensure proper alignment
4. Commit and push

To change styling:
1. Edit the `<style>` section in index.html
2. Test locally
3. Commit and push