from flask import Blueprint, render_template, request, \
    redirect, url_for

# Logging
import logging
logger = logging.getLogger(__name__)


home = Blueprint('home', __name__)
home.config = {}


@home.record
def record_params(setup_state):
  app = setup_state.app
  home.config = dict([(key, value) for (key, value) in app.config.items()])


# Basic site routes
@home.route('/', methods=['GET'])
def index():
    """ Main page """
    return render_template('index.html')


@home.route('/maillist', methods=['POST'])
def maillist_post():
    """ Subscribe to mail list endpoint """
    # TODO send to mail list later on
    email = request.form.get('email')
    logger.info(f"email: {email}")
    return redirect(url_for("home.index"))
