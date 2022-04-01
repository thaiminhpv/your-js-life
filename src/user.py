from . import model
from unicodedata import name
from flask import Flask, redirect, url_for, render_template, request, session, Blueprint
import cloudinary.uploader
from dotenv import load_dotenv
import os
from .dataprovider import InteractDatabse
from pymysql import NULL
from mysql.connector import connect, Error
load_dotenv()

user = Blueprint("user", __name__)

cloudinary.config(
    cloud_name='dxu6nsoye',
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECREAT'),
)

data_user = model.Users()
path = "https://res.cloudinary.com/dxu6nsoye/image/upload/v1648535365/ihzghstemlzcobhbbfzg.jpg"


@user.route("/portfolio", methods=["GET"])
def user_home():
    global data_user
    global path
    # TODO: extract /portfolio?id=<id>
    return render_template("generated-portfolio.html", user=data_user, image_path=path)


@user.route("/create-portfolio", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        global data_user 
        data_user = model.Users.getdatafromrequest(request.form)
        #id = InteractDatabse.test(data_user.name)    #add data user to database and get id of this user
        data_user.name = id
        file = request.files['file']
        if file:  #check if user has uploaded file, save the path
            global path
            res = cloudinary.uploader.upload(file)
            path = res['secure_url']
            #InteractDatabase.savepath(id,path)      #save avt path user
        return redirect(url_for('user.user_home'))
    return render_template("input-page.html")


@user.route("/", methods=["GET"])
def home():
    return render_template("generated-portfolio.html")


