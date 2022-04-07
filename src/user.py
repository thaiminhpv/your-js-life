from . import model
from unicodedata import name
from flask import Flask, jsonify, redirect, url_for, render_template, request, session, Blueprint
import cloudinary.uploader
from dotenv import load_dotenv
import os
from .dataprovider import InteractDatabase, get_id
from pymysql import NULL
from mysql.connector import connect, Error
import json

load_dotenv()

data_user = model.Users()
path = ""

user = Blueprint("user", __name__)

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECREAT'),
)


@user.route("/portfolio/<id>", methods=["GET"])
def user_home(id):
    global data_user
    global path
    user = InteractDatabase.getportfolio(id)
    exp = InteractDatabase.get_exp(id)
    edu = InteractDatabase.get_edu(id)
    return render_template('generated-portfolio.html', user = user, image_path = path, experience = exp, education = edu)


# @user.route("/create-portfolio", methods=["POST", "GET"])
# def index():
#     if request.method == "POST":
#         global data_user
#         data_user = model.Users.getdatafromrequest(request.form)
#         id = InteractDatabase.test(data_user.name)    #add data user to database and get id of this user
#         file = request.files['file']
#         if file:  #check if user has uploaded file, save the path
#             global path
#             res = cloudinary.uploader.upload(file)
#             path = res['secure_url']
#             #InteractDatabase.savepath(id,path)      #save avt path user
#         return redirect(url_for('user.user_home'))
#     return render_template("input-page.html")


@user.route("/", methods=["GET"])
def home():
    return render_template("landing-page.html")


@user.route("/create-portfolio", methods=["POST", "GET"])
def index():
    global path
    #data_user = model.Users.getdatafromrequest(request.form)
    #id = InteractDatabase.addportfolio(data_user)     # add data user to database and get id of this user        
    #path = get_path_image()     # save avt and get path user's avt from cloud
    #InteractDatabase.save_path_to_database(id, path)
    id = 1
    request_json = request.json
    exp = request_json["experience"]
    edu = request_json["education"]
    InteractDatabase.save_exp(id, exp)
    InteractDatabase.save_edu(id,edu)
    return "successful"


# method
def get_path_image():
    file = request.files['file']
    # check if user has uploaded file, save the path
    if file:
        res = cloudinary.uploader.upload(file)
        return res['secure_url']
    else:
        return "https://res.cloudinary.com/dxu6nsoye/image/upload/v1648535365/ihzghstemlzcobhbbfzg.jpg"
