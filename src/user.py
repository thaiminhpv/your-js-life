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

user = Blueprint("user", __name__)

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECREAT'),
)

@user.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        render_template(url_for('user.register'))
    elif request.method == "GET":
        return render_template("landing-page.html")


@user.route("/create-portfolio", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        id = handle_data(request)
        return redirect(url_for('user.portfolio', id = id))
        #return id
    elif request.method == "GET":
        return render_template("input-page.html")


@user.route("/portfolio/<id>", methods=["GET"])
def portfolio(id):
    data_user = InteractDatabase.getportfolio(id)
    path = InteractDatabase.get_path_image(id)
    experience = InteractDatabase.get_exp(id)
    education = InteractDatabase.get_edu(id)
    services = InteractDatabase.get_services(id)
    skills = InteractDatabase.get_skills(id)
    return render_template('generated-portfolio.html', user = data_user, image_path = path, experience = experience, education = education, services = services, skills = skills)


#method
    """    handle_data
    get data from request
    save data to database ( data_user, experience, education, service, skills, path of image)
    """

def handle_data(request):
    data_user = model.Users.getdatafromrequest(request.form)
    id = InteractDatabase.addportfolio(data_user)       # add data user to database and get id of this user

    # request_json = request.json
    # experience = request_json["experience"]
    # InteractDatabase.save_exp(id, experience)

    # education = request_json["education"]
    # InteractDatabase.save_edu(id, education)

    # services = request_json["services"]
    # InteractDatabase.save_services(id, services)

    # skills = request_json["skills"]
    # InteractDatabase.save_skills(id, skills)

    path = get_path_image(request)     # save avt and get path user's avt from cloud
    InteractDatabase.save_path_to_database(id, path)
    return id


def get_path_image(request):
    file = request.files['file']
    # check if user has uploaded file, save the path
    if file:
        res = cloudinary.uploader.upload(file)
        return res['secure_url']
    else:
        return "https://res.cloudinary.com/dxu6nsoye/image/upload/v1648535365/ihzghstemlzcobhbbfzg.jpg"
