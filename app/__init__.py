from flask import Flask
from .models import db
from .admin import init_admin
from .views import main

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    #db config
    app.config.from_object("config")

    db.init_app(app)
    init_admin(app)
    app.register_blueprint(main)

    return app