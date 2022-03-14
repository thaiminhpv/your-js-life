#from crypt import methods
from flask_login import current_user
from . import model
import imp
from unicodedata import name
from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
user = Blueprint("user", __name__)
data_user = model.users()

@user.route("/home")
def user_home():
    user = convert()
    return render_template("page2.html",user = user )

@user.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        GetDataRequest()
        return redirect(url_for('user.user_home'))
    return render_template("index.html")



# convert model to dict
def convert():
    mydict = dict(firstname=data_user.first_name, lastname =data_user.last_name,language =data_user.Language,email= data_user.email,nation= data_user.nation, age =data_user.age, address = data_user.address)
    return mydict

def GetDataRequest():
    data_user.first_name = request.form["firstname"]
    data_user.last_name = request.form["lastname"]
    data_user.email = request.form["email"]
    data_user.nation = request.form["nation"]
    data_user.age = request.form["age"]
    data_user.Language = request.form["selectLanguage"]
    data_user.address = request.form["address"]
