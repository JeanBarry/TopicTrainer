from flask import Flask
from src.router import router
from src.api import create_api


def create_app() -> Flask:
    """
    Create a Flask app using the app factory pattern.
    Pass the app to the router function to register routes.
    Pass the app to the create_api function to register the API.
    :return: Flask app
    """

    app = Flask(__name__)
    router(app)
    create_api(app)

    return app
