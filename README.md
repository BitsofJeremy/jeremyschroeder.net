# jeremyschroeder.net

A minimalist personal website featuring ASCII art logo on a dark background.

![screenshot](screenshot.png)

## Overview

This is a static HTML website designed to be hosted on GitHub Pages. The site features:
- Clean, minimalist design with green ASCII art logo
- Black background with glowing text effect
- Responsive design for mobile devices
- Zero dependencies - just HTML and CSS

## Structure

```
.
├── index.html              # Main HTML file
├── static/
│   └── images/
│       ├── favicon.ico     # Site favicon
│       ├── profile.jpeg    # Profile image
│       └── background.mp4  # Background video (archived)
├── .nojekyll              # GitHub Pages configuration
└── README.md              # This file
```

## Deployment

### GitHub Pages

This site is configured for GitHub Pages deployment:

1. Push your changes to the main branch
2. Go to your repository settings on GitHub
3. Navigate to Pages section
4. Select the branch to deploy (usually `main`)
5. Select `/` (root) as the source directory
6. Save and wait for deployment

Your site will be available at: `https://[username].github.io/jeremyschroeder.net/`

### Local Development

Simply open `index.html` in your web browser:

```bash
# Using Python's built-in server
python -m http.server 8000

# Or just open the file directly
open index.html  # macOS
xdg-open index.html  # Linux
start index.html  # Windows
```

## Customization

The site styling can be customized by editing the `<style>` section in `index.html`:
- Background color: `#000000` (black)
- Text color: `#00ff00` (green)
- Font: Courier New (monospace)
- Text shadow: `0 0 5px #00ff00` (glow effect)

## License

See LICENSE file for details.
