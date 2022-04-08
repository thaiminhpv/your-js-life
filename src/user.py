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
    if id != 'None':
        data = InteractDatabase.get_all(id)
        temp = data[0]
        data_user = dict(
            id=temp[0],
            name=temp[1],
            gmail=temp[2],
            phone=temp[3],
            address=temp[4],
            dateofbirth=temp[5],
            linkedin=temp[6],
            facebook=temp[7],
            github=temp[8],
            job=temp[9],
            workingtime=temp[10],
            introduction=temp[11],
        )
        path = temp[12]
        education = [_[13] for _ in data]  # = data[:, 13].T in numpy
        services = [_[14] for _ in data]
        experience = [_[15] for _ in data]
        skills = [_[16] for _ in data]

        return render_template(
            'generated-portfolio.html',
            user=data_user, image_path=path, experience=experience,
            education=education, services=services, skills=skills
        )
    else:
        return redirect(url_for('user.register'))


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

    path = get_path_image(request)     # get path user's avt from cloud
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
