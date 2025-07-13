from flask import Flask, redirect, url_for, render_template
from app import app

@app.route("/")
def home():
    return redirect(url_for("blog"))

@app.route("/blog")
def blog():
    return render_template("blog.html")