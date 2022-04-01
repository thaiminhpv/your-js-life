from . import model
from unicodedata import name
from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
import cloudinary.uploader
from dotenv import load_dotenv
import os

load_dotenv()

user = Blueprint("user", __name__)

cloudinary.config(

    cloud_name='dxu6nsoye',
    api_key= os.getenv('API_KEY'),
    api_secret= os.getenv('API_SECREAT') ,
)

data_user = model.Users()
path = ""


@user.route("/home")
def user_home():
    global data_user
    global path
    return render_template("page2.html",user = data_user, image_path = path )

@user.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        GetDataRequest()
        if request.files:
            global path
            file = request.files.get('file')
            res = cloudinary.uploader.upload(file)
            path = res['secure_url']
            print(path)
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
