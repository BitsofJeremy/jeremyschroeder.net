# config.py

import os
from datetime import timedelta

# Put any configurations here that are common across all environments

# App Version Number
APP_VERSION = '0.0.1'

# Name of the app
APP_NAME = 'app'
HOST = '127.0.0.1'
PORT = '5052'

# Get our environment
FLASK_ENV = os.getenv('FLASK_ENV')
# Set debug mode
if FLASK_ENV == 'production':
    DEBUG = False
else:
    DEBUG = True

# Some Flask App Config settings
SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME')
# SESSION_COOKIE_SECURE = True

# Session timeout set to 4 hours
PERMANENT_SESSION_LIFETIME = timedelta(hours=4)

# Threads
THREADS_PER_PAGE = 2

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = os.urandom(32).hex()

# Secret key for signing cookies
SECRET_KEY = os.urandom(32).hex()

# Mailgun config
DOMAIN_NAME = os.getenv('DOMAIN_NAME')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
