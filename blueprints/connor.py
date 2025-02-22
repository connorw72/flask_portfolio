from flask import Blueprint, render_template
import requests
from algorithms.petinfo import pinfo
from pathlib import Path

bconnor = Blueprint("bconnor", __name__, static_folder="static", template_folder="templates")

@bconnor.route('/connor/')
def connor():
    url = "https://genius.p.rapidapi.com/artists/16775/songs"

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "e96b80de18msh080ccecb09304e3p1f9084jsn90d405c70ce3"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()['response']['songs']

    print(data)
    return render_template('connor.html', data=data)

@bconnor.route('/petapi/')
def petapi():
    url = "https://api.adoptapet.com/search/pets_at_shelter"

    headers = {
        'host': "api.adoptapet.com",
        'key': "A34F48&v"
    }

    response = requests.request("GET", url, headers=headers)
    data2 = response.json()['shelter_id']

    print(data2)
    return render_template('petapi.html', data2=data2)


@bconnor.route('/PetInfo/')
def PetInfo():
    path = Path(bconnor.root_path) / "testconnorimages"
    return render_template('PetInfo.html', pimage=pinfo(path))

@bconnor.route('/PetQuiz/')
def PetQuiz():
    return render_template('PetQuiz.html')

@bconnor.route('/google/')
def google():
    return render_template('google.html')

@bconnor.route('/map/')
def map():
    return render_template('map.html')

@bconnor.route('/testquiz/')
def testquiz():
    return render_template('testquiz.html')

@bconnor.route('/Jeopardy/')
def Jeopardy():
    return render_template('Jeopardy.html')



