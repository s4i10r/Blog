from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Blogpost {self.title}>"