from flask import Flask


def create_app():
    """
    Create a Flask app using the app factory pattern.

    :return: Flask app
    """

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Index'

    return app
