from flask import Flask
from .models import db
from .views import main

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    #db config
    app.config.from_object("config")
    db.init_app(app)

    with app.app_context():
        db.create_all()


    app.register_blueprint(main)

    return app