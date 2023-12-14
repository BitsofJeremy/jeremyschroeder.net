
# external imports
from flask import Blueprint, render_template, request, \
    redirect, url_for, flash, jsonify
import requests

# Logging
import logging
logger = logging.getLogger(__name__)


home = Blueprint('home', __name__)
home.config = {}


@home.record
def record_params(setup_state):
  app = setup_state.app
  home.config = dict([(key, value) for (key, value) in app.config.items()])

# Helper functions


# def add_list_member(email):
#     MAILLIST = home.config['MAILGUN_MAILLIST']
#     MAILGUN_API_KEY = home.config['MAILGUN_API_KEY']
#     # TODO Add try/except for request fails
#     logger.info(f"Adding {email} to mail list")
#     return requests.post(
#         f"https://api.mailgun.net/v3/lists/{MAILLIST}/members",
#         auth=('api', MAILGUN_API_KEY),
#         data={
#             'subscribed': True,
#             'address': email
#         }
#     )
#
#
# def send_welcome_message(email):
#     MAILGUN_API_KEY = home.config['MAILGUN_API_KEY']
#     return requests.post(
#         "https://api.mailgun.net/v3/email.beforegreatness.com/messages",
#         auth=(
#             "api",
#             MAILGUN_API_KEY
#         ),
#         data={
#             "from": "Jeremy Schroeder <jeremy@beforegreatness.com>",
#             "to": email,
#             "subject": "Welcome to the Before Greatness Family!",
#             "template": "thank-you-for-subscribing"
#         }
#     )


# Basic site routes
@home.route('/', methods=['GET'])
def index():
    """ Main page """
    # uncomment to add logos
    # logo_url = url_for('static', filename='images/logo.png')
    # brand_logo_url = url_for('static', filename='images/LOGO.png')
    video_url = url_for(
        'static',
        filename='videos/background_video.mp4'
    )
    return render_template(
        'index.html',
        video_url=video_url,
        # logo_url=logo_url,
        # brand_logo_url=brand_logo_url
    )


# @home.route('/about', methods=['GET'])
# def about():
#     """ About Us page """
#     uncomment to add logos
#     logo_url = url_for('static', filename='images/logo.png')
#     brand_logo_url = url_for('static', filename='images/LOGO.png')
#     video_url = url_for(
#         'static',
#         filename='videos/background_video.mp4'
#     )
#     return render_template(
#         'about.html',
#         video_url=video_url,
#         logo_url=logo_url,
#         brand_logo_url=brand_logo_url
#     )


# @home.route('/maillist', methods=['POST'])
# def maillist_post():
#     """ Subscribe to mail list endpoint """
#     email = request.form.get('email')
#     added = add_list_member(email=email)
#     flash("Thank you for your interest, please check your email for updates.")
#     logger.info(added.text)
#     # Send thank you message
#     send_welcome_message(email=email)
#     return render_template('index.html')
