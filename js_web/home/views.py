from flask import Blueprint, render_template, request, \
    redirect, url_for
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


def send_simple_message(name, email, message):
    """
    Taken from Mailgun docs to send from /contact form
    """
    url = f"https://api.mailgun.net/v3/{home.config['DOMAIN_NAME']}/messages"
    data = {
        "from": f"{email}",
        "to": [f"{home.config['ADMIN_EMAIL']}"],
        "subject": f"[jeremyschroeder.net] Website Request",
        "text": f"Message:  {message} \n\nName:  {name} \n\nEmail:  {email}"}
    logger.debug(url)
    logger.debug(data)
    res = requests.post(
        url,
        auth=("api", home.config['MAILGUN_API_KEY']),
        data=data
    )
    logger.info(res.text)
    return True


# Basic site routes
@home.route('/', methods=['GET'])
def index():
    """ Main page """
    return render_template('index.html')


@home.route('/contact', methods=['POST'])
def contact():
    """
    Sends info from /contact POST form to
    admin email via Mailgun.
    """
    # get post args
    data = request.form
    name = data['name']
    email = data['email']
    message = data['message']
    logger.info(f"Someone Entered: {name}, \
          {email}, {message}")
    _res = send_simple_message(name, email, message)
    if _res:
        logger.info("Message Sent!")
    else:
        logger.info("Something went wrong with message.")
    return redirect(url_for("home.index"))
