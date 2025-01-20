from datetime import timedelta
import os
from flask import Flask, render_template
import logging
from logging.handlers import RotatingFileHandler


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


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
