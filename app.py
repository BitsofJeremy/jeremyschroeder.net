"""js_web app"""
# Import the app
from js_web import app


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
    )
