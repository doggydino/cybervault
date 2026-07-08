from flask import Flask, render_template, request, redirect, url_for

from auth.login import login_user
from auth.register import register_user

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if register_user(username, password):
            return render_template("registration_success.html")

        return "Username already exists."

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if login_user(username, password):
            return "Login successful."

        return "Invalid username or password."

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)