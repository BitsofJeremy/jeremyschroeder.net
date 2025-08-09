from datetime import timedelta, datetime
import os
from flask import Flask, render_template, jsonify
import logging
from logging.handlers import RotatingFileHandler
import requests


# App initialization
app = Flask(__name__)

# App configuration
app.config['APP_VERSION'] = '0.0.5'
app.config['APP_NAME'] = 'jeremyschroeder.net'
app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 5052

# Environment settings
app.config['FLASK_ENV'] = os.environ.get('FLASK_ENV', 'production')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

# Ghost API settings
app.config['GHOST_API_KEY'] = os.environ.get('GHOST_API_KEY')
app.config['GHOST_API_URL'] = 'https://bits.jeremyschroeder.net/ghost/api/content'

# Security settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(32).hex())
app.config['CSRF_SESSION_KEY'] = os.environ.get('CSRF_SESSION_KEY', os.urandom(32).hex())
app.config['SESSION_COOKIE_NAME'] = os.environ.get('SESSION_COOKIE_NAME', 'jeremyschroeder.net')
app.config['SESSION_COOKIE_SECURE'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=4)

# CSRF protection
app.config['CSRF_ENABLED'] = True


# Logging configuration
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/jeremyschroeder.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('*** JeremySchroeder.net startup ***')


@app.template_filter('datetime_format')
def datetime_format(value):
    """Format datetime string from Ghost API"""
    if not value:
        return ''
    try:
        # Parse ISO format datetime from Ghost API
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        return dt.strftime('%B %d, %Y')
    except (ValueError, AttributeError):
        return value


@app.route('/')
def index():
    blog_posts = get_recent_posts()
    return render_template('index.html', blog_posts=blog_posts)


@app.route('/api/posts')
def api_posts():
    posts = get_recent_posts()
    return jsonify(posts)


def get_recent_posts():
    """Fetch up to 3 recent posts from Ghost API"""
    if not app.config['GHOST_API_KEY']:
        app.logger.warning('Ghost API key not configured')
        return []
    
    try:
        response = requests.get(
            f"{app.config['GHOST_API_URL']}/posts/",
            params={
                'key': app.config['GHOST_API_KEY'],
                'limit': 3,
                'fields': 'title,slug,excerpt,published_at,url',
                'formats': 'html'
            },
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            return data.get('posts', [])
        else:
            app.logger.error(f'Ghost API error: {response.status_code}')
            return []
            
    except requests.RequestException as e:
        app.logger.error(f'Error fetching Ghost posts: {e}')
        return []


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
