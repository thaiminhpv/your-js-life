from time import time
import json
from tokenize import String
import cloudinary.uploader
from flask import redirect, template_rendered, url_for, render_template, request, Blueprint, Response, jsonify, abort
from . import config
from . import model
from .dataprovider import InteractDatabase
from src import dataprovider
import time
from .emojify import convert_obj_to_emoji

user = Blueprint("user", __name__)


@user.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("landing-page.html")
    if request.method == "POST":
        return redirect(url_for('user.create_portfolio_data_user'))

@user.route("/home", methods=["GET"])
def create_portfolio_data_user():
    if request.method == "GET":
        return render_template("input-page.html")

@user.route("/home", methods=["POST"])
def create_portfolio_file():
    try:
        dataprovider.InteractDatabase.save_data(request.form)
        return render_template("success.html")
    except:
        return render_template("404.html")

# @user.route("/create-portfolio", methods=["POST"])
# def create_portfolio_file():
#     print(123)
#     data = model.Users.getdatafromrequest(request.json)
#    if data == "-1":
#         return Response(data, status=400)
#     else:
#         print(data['name'])


# @user.route("/create-portfolio/file", methods=["POST"])
# def register():
#     id = request.form['id']
#     path = get_path_image(request)
#     InteractDatabase.save_path_to_database(id, path)
#     return jsonify({"id": id, "status": "success"})


# @user.route("/portfolio/<id>", methods=["GET"])
# def portfolio(id):
#     data = InteractDatabase.get_user_data_from_id(id)
#     if data is None:
#         abort(404)  # not found

#     data_user = data['user']
#     path = data['path']
#     education = data['education']
#     services = data['services']
#     experience = data['experience']
#     skills = data['skills']

#     # if params emoji exist (/portfolio/<id>?emoji=true), then convert all string characters to emoji
#     if request.args.get('emoji') == 'true':
#         data_user = convert_obj_to_emoji(data_user)
#         education = convert_obj_to_emoji(education)
#         services = convert_obj_to_emoji(services)
#         experience = convert_obj_to_emoji(experience)
#         skills = convert_obj_to_emoji(skills)

#     # pretty_print_json(data_user=data_user, path=path, education=education, services=services, experience=experience, skills=skills)

#     education = [e for e in education if e.get('title') and e.get('time') and e.get('content')]
#     experience = [e for e in experience if e.get('title') and e.get('time') and e.get('content')]
#     services = [s for s in services if s.get('description') and s.get('title')]
#     skills = [s for s in skills if s.get('skill')]

#     return render_template(
#         'generated-portfolio.html',
#         user=data_user, image_path=path, experience=experience,
#         education=education, services=services, skills=skills
#     )


# def pretty_print_json(**kwargs):
#     temp = dict(**kwargs)
#     # pretty print json
#     print(json.dumps(temp, indent=4, sort_keys=True))


# @user.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"), 404


# @user.route("/success", methods=["GET"])
# def success():
#     return render_template("success.html")


# def get_path_image(request):
#     file = request.files.get('file', None)
#     # check if user has uploaded file, save the path
#     if file is not None:
#         res = cloudinary.uploader.upload(file)
#         return res['secure_url']
#     else:
#         return "https://res.cloudinary.com/dxu6nsoye/image/upload/v1649821452/z3336574163217_bc5927ec38c68b516f13b300443dfcac_zouzvp.jpg"
