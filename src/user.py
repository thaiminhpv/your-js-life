import threading
from time import time
import cloudinary.uploader
from flask import redirect, template_rendered, url_for, render_template, request, Blueprint, Response, jsonify, abort
from . import config
from . import model
from .dataprovider import InteractDatabase
from src import dataprovider
import time

user = Blueprint("user", __name__)


@user.route("/", methods=["GET"])
def home():
    MAX_DESCRIPTION_LENGTH = 15
    portfolios_tuple = InteractDatabase.get_all_portfolio()
    portfolios = list(map(list, portfolios_tuple))  # convert list of tuple to list of list
    for index, portfolio in enumerate(portfolios):
        if len(portfolio[2]) > MAX_DESCRIPTION_LENGTH:
            portfolios[index][2] = portfolio[2][:MAX_DESCRIPTION_LENGTH] + "..."
    print(portfolios)
    return render_template("landing-page.html", portfolios=portfolios)


@user.route("/create-portfolio", methods=["GET"])
def create_portfolio_data_user():
    return render_template("input-page.html")


@user.route("/create-portfolio", methods=["POST"])
def create_portfolio_file():
    data = model.Users.getdatafromrequest(request.json)
    id = dataprovider.get_id()
    threading.Thread(target=save_data, args=(id, data)).start()
    return Response(str(id), status=200)


@user.route("/create-portfolio/file", methods=["POST"])
def register():
    id = request.form['id']
    path = get_path_image(request)
    InteractDatabase.save_path_to_database(id, path)
    return jsonify({"id": id, "status": "success"})


@user.route("/portfolio/<id>", methods=["GET"])
def portfolio(id):
    data = InteractDatabase.get_user_data_from_id(id)
    if data is None:
        abort(404)  # not found

    data_user = data['user']
    path = data['path']
    education = data['education']
    services = data['services']
    experience = data['experience']
    skills = data['skills']

    return render_template(
        'generated-portfolio.html',
        user=data_user, image_path=path, experience=experience,
        education=education, services=services, skills=skills
    )


@user.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@user.route("/success", methods=["GET"])
def success():
    return render_template("success.html")


def save_data(id, data):
    InteractDatabase.addportfolio(data['user'])
    InteractDatabase.save_exp(id, data['experience'])
    InteractDatabase.save_edu(id, data['education'])
    InteractDatabase.save_services(id, data['services'])
    InteractDatabase.save_skills(id, data['skills'])
   

def get_path_image(request):
    file = request.files.get('file', None)
    # check if user has uploaded file, save the path
    if file:
        res = cloudinary.uploader.upload(file)
        return res['secure_url']
    else:
        return "https://res.cloudinary.com/dxu6nsoye/image/upload/v1648535365/ihzghstemlzcobhbbfzg.jpg"