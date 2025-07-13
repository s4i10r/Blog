from flask import Blueprint, redirect, url_for, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return redirect(url_for("blog"))

@main.route("/blog")
def blog():
    return render_template("blog.html")