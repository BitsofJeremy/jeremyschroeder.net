# Import the Flask basics
from logging.config import dictConfig
from flask import Flask, flash, redirect, url_for

# define logging dict
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '{"date": "%(asctime)s", '
                      '"log_level": "%(levelname)s", '
                      '"module": "%(module)s", '
                      '"message": "%(message)s"}'
         }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'app.log',
            'maxBytes': 1024000,
            'backupCount': 3
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': [
            'wsgi',
            'file'
        ]
    }
})

# Define the App
app = Flask(__name__)

# Pull in the config
app.config.from_pyfile('../config.py')

# Import the module / component using their blueprints
# Initial frontend views
from js_web.home.views import home

# Register the Blueprints with the app
app.register_blueprint(home)
