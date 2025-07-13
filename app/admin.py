from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import db, Blogpost

def init_admin(app):
    admin = Admin(app, name="Admin", template_mode="bootstrap3")
    admin.add_view(ModelView(Blogpost, db.session))