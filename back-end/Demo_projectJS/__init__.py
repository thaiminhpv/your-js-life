from django.apps import AppConfig
from flask import Flask
import os
from dotenv import load_dotenv
from .user import user
import imp



def create_app():
    app = Flask(__name__)
    app.register_blueprint(user)
    return app


