from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests
from __init__ import db
from crud2.model import Centers

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_crud_center = Blueprint('centercrud', __name__,
                     url_prefix='/centercrud',
                     template_folder='templates/crud/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud_center)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# User/Users extraction from SQL
def center_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Centers.query.all()]


def center_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Centers.query.filter((Centers.centerName.ilike(term)) | (Centers.location.ilike(term)) | (Centers.email.ilike(term)) | (Centers.phone.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def center_by_id(centerID):
    """finds User in table matching userid """
    return Centers.query.filter_by(centerID=centerID).first()

def center_by_name(centerName):
    """finds User in table matching email """
    return Centers.query.filter_by(centerName=centerName).first()


# Default URL
# Default URL
@app_crud_center.route('/')
def crudAC():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crudAC.html", table=center_all())


# CRUD create/add
@app_crud_center.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Centers(
            request.form.get("centerName"),
            request.form.get("location"),
            request.form.get("email"),
            request.form.get("phone")
        )
        po.create()
    return redirect(url_for('centercrud.crudAC'))

# CRUD create/add
@app_crud_center.route('/createCenter/', methods=["POST"])
def createCenter():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Centers(
            request.form.get("centerName"),
            request.form.get("location"),
            request.form.get("email"),
            request.form.get("phone")
        )
        po.create()
    return redirect(url_for('centercrud.search'))


# CRUD read
@app_crud_center.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        centerID = request.form.get("centerid")
        po = center_by_id(centerID)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crudAC.html", table=table)


# CRUD update
@app_crud_center.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        centerID = request.form.get("centerid")
        centerName = request.form.get("centerName")
        location = request.form.get("location")
        email = request.form.get("email")
        phone = request.form.get("phone")
        po = center_by_id(centerID)
        if po is not None:
            po.update(centerName)
            po.update(location)
            po.update(email)
            po.update(phone)
    return redirect(url_for('centercrud.crudAC'))


# CRUD delete
@app_crud_center.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        # Getting centerid from the form in the HTML; centerid is there, not centerID; centerID is the column
        centerID = request.form.get("centerid")
        po = center_by_id(centerID)
        if po is not None:
            po.delete()
    return redirect(url_for('centercrud.crudAC'))

# Search Form
@app_crud_center.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("centerSearch.html")


# Search request and response
@app_crud_center.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(center_ilike(term)), 200)
    return response









