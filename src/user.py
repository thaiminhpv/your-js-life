import threading
from time import time
import cloudinary.uploader
from flask import redirect, template_rendered, url_for, render_template, request, Blueprint
from . import config 
from . import model
from .dataprovider import InteractDatabase
from src import dataprovider
import time
user = Blueprint("user", __name__)


@user.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        render_template(url_for('user.register'))
    elif request.method == "GET":
        MAX_DESCRIPTION_LENGTH = 15
        portfolios_tuple = InteractDatabase.get_all_portfolio()
        portfolios = list(map(list, portfolios_tuple))  # convert list of tuple to list of list
        for index, portfolio in enumerate(portfolios):
            if len(portfolio[2]) > MAX_DESCRIPTION_LENGTH:
                portfolios[index][2] = portfolio[2][:MAX_DESCRIPTION_LENGTH] + "..."

        return render_template("landing-page.html", portfolios=portfolios)


@user.route("/create-portfolio", methods=["POST", "GET"])
def register():
    config.post_request = request.json
    if request.method == "POST":
        id = dataprovider.get_id()
        return redirect(url_for('user.portfolio', id = id))
    elif request.method == "GET":
        return render_template("input-page.html")
        

@user.route("/portfolio/<id>", methods=["GET"])
def portfolio(id):
    temp = dataprovider.get_id()
    if id == temp:
        return get_data(id)
    elif id != temp:
        data = InteractDatabase.get_user_data_from_id(id)

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

    else:
        return redirect(url_for('user.register'))

 

def get_data(id):
    request_json = config.post_request   

    data_user = model.Users.getdatafromrequest(request_json)
    #path = get_path_image(request)  # get path user's avt from cloud
    path = "https://res.cloudinary.com/dxu6nsoye/image/upload/v1648535365/ihzghstemlzcobhbbfzg.jpg"
    experience = request_json["experience"]
    education = request_json["education"]
    services = request_json["services"]
    skills = request_json["skills"]
    
    threading.Thread(target=save_data, args=(id, data_user, experience, education, services, skills, path)).start()
    
    #return "successful"
    return render_template(
        'generated-portfolio.html',
        user=data_user, image_path=path, experience=experience,
        education=education, services=services, skills=skills
    )



def save_data(id, data_user, experience, education, services, skills, path):
    InteractDatabase.addportfolio(data_user)  
    InteractDatabase.save_exp(id, experience)
    InteractDatabase.save_edu(id, education)
    InteractDatabase.save_services(id, services)
    InteractDatabase.save_skills(id, skills)
    InteractDatabase.save_path_to_database(id, path)


def get_path_image(request):
    file = request.files['file']
    # check if user has uploaded file, save the path
    if file:
        res = cloudinary.uploader.upload(file)
        return res['secure_url']
    else:
        return "https://res.cloudinary.com/dxu6nsoye/image/upload/v1648535365/ihzghstemlzcobhbbfzg.jpg"

