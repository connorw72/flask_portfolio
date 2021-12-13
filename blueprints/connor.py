from flask import Blueprint, render_template
import requests

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