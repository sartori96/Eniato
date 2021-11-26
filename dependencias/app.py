from flask import Flask
from dependencias.ext import site

def create_app(app):
    app = Flask(__name__)
    site.init_app(app)
    return app