#from crypt import methods
import email
import imp
from flask import Flask, redirect, url_for, render_template, request, session, Blueprint

user = Blueprint("user", __name__)

@user.route("/home")
def user_home():
    return render_template("page2.html")

@user.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
       # user_email = request.form["email"]
        return redirect(url_for('user.user_home'))
    return render_template("index.html")

