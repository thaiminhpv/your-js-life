import cloudinary.uploader
from flask import redirect, url_for, render_template, request, Blueprint

from . import model
from .dataprovider import InteractDatabase

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
    if request.method == "POST":
        id = handle_data(request)
        return redirect(url_for('user.portfolio', id=id))
        # return id
    elif request.method == "GET":
        return render_template("input-page.html")


@user.route("/portfolio/<id>", methods=["GET"])
def portfolio(id):
    if id != 'None':
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


def handle_data(request):
    """
    get data from request
    save data to database ( data_user, experience, education, service, skills, path of image)
    :param request:
    :return:
    """
    data_user = model.Users.getdatafromrequest(request.form)
    id = InteractDatabase.addportfolio(data_user)  # add data user to database and get id of this user

    # request_json = request.json
    # experience = request_json["experience"]
    # InteractDatabase.save_exp(id, experience)

    # education = request_json["education"]
    # InteractDatabase.save_edu(id, education)

    # services = request_json["services"]
    # InteractDatabase.save_services(id, services)

    # skills = request_json["skills"]
    # InteractDatabase.save_skills(id, skills)

    path = get_path_image(request)  # get path user's avt from cloud
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
