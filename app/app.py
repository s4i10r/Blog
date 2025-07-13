from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("blog"))

@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run(debug=True)