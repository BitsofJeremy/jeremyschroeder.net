import os
from flask import Flask, render_template, request, flash, jsonify
import requests
from datetime import timedelta
import logging
from logging.handlers import RotatingFileHandler
from flask_simple_captcha import CAPTCHA

# App initialization
app = Flask(__name__)

# App configuration
app.config['APP_VERSION'] = '0.0.3'
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

# Mailgun configuration
app.config['DOMAIN_NAME'] = os.environ.get('DOMAIN_NAME')
app.config['ADMIN_EMAIL'] = os.environ.get('ADMIN_EMAIL')
app.config['MAILGUN_API_KEY'] = os.environ.get('MAILGUN_API_KEY')

# CAPTCHA configuration
CAPTCHA_CONFIG = {
    'SECRET_CAPTCHA_KEY': os.environ.get('SECRET_CAPTCHA_KEY', os.urandom(32).hex()),
    'EXPIRE_SECONDS': 60 * 10,  # 10 minutes
    'CAPTCHA_IMG_FORMAT': 'JPEG',
    'CAPTCHA_LENGTH': 6,
    'CAPTCHA_DIGITS': False,
    'EXCLUDE_VISUALLY_SIMILAR': True,
    'BACKGROUND_COLOR': (40, 44, 52),  # Dark background color (282c34)
    'TEXT_COLOR': (97, 175, 239),  # Light blue text color (61afef)
    'ONLY_UPPERCASE': True,
}
SIMPLE_CAPTCHA = CAPTCHA(config=CAPTCHA_CONFIG)
app = SIMPLE_CAPTCHA.init_app(app)

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
    new_captcha = SIMPLE_CAPTCHA.create()
    return render_template('index.html', captcha=new_captcha)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    captcha_hash = request.form.get('captcha-hash')
    captcha_text = request.form.get('captcha-text')

    if SIMPLE_CAPTCHA.verify(captcha_text, captcha_hash):
        if send_email(name, email, message):
            flash("Thank you for your message! We'll get back to you soon.", "success")
            app.logger.info(f"Contact form submitted successfully by {email}")
            return jsonify({"status": "success"})
        else:
            flash("An error occurred while sending your message. Please try again later.", "error")
            app.logger.error(f"Failed to send email from {email}")
            return jsonify({"status": "error", "message": "Failed to send email"})
    else:
        flash("CAPTCHA verification failed. Please try again.", "error")
        app.logger.warning(f"Failed CAPTCHA attempt from {email}")
        return jsonify({"status": "error", "message": "CAPTCHA verification failed"})

def send_email(name, email, message):
    url = f"https://api.mailgun.net/v3/{app.config['DOMAIN_NAME']}/messages"
    data = {
        "from": f"{name} <{email}>",
        "to": [app.config['ADMIN_EMAIL']],
        "subject": "[jeremyschroeder.net] New Contact Form Submission",
        "text": f"Name: {name}\nEmail: {email}\n\nMessage: {message}"
    }
    try:
        response = requests.post(
            url,
            auth=("api", app.config['MAILGUN_API_KEY']),
            data=data
        )
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        app.logger.error(f"Mailgun API error: {str(e)}")
        return False

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )