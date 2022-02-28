from flask import Blueprint, render_template
import requests

bpranav = Blueprint("bpranav", __name__, static_folder="static", template_folder="templates")

@bpranav.route('/pranav/')
def pranav():
    return render_template('pranav.html')

@bpranav.route('/dogs/')
def dogs():
    return render_template('dogs.html')

@bpranav.route('/birds/')
def birds():
    return render_template('birds.html')

@bpranav.route('/petplanner/')
def petplanner():
    return render_template('petplanner.html')

@bpranav.route('/imagechange/')
def imagechange():
    return render_template('imagechange.html')

@bpranav.route('/wordle/')
def wordle():
    return render_template('wordle.html')

@bpranav.route('/wordle2/')
def wordle2():
    return render_template('wordle2.html')