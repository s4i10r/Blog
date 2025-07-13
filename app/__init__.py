from flask import Flask
from .models import db
from .admin import init_admin

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

    db.init_app(app)
    init_admin(app)

    return app