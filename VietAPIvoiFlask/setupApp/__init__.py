from flask import Flask, request, Blueprint
# from books.controller import books
from .books.controller import books

def createApp(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    print(app.config['SECRET_KEY'])
    app.register_blueprint(books)
    
    return app

