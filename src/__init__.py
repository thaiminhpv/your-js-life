from flask import Flask
from .config import *
from .user import user


# import imp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user)
    return app
