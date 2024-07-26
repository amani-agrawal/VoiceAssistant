from flask import Flask
from os import path


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfghjklp qwertyuiop'

    from .search import search
    
    app.register_blueprint(search, url_prefix='/')
    return app