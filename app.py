from flask import Flask, render_template, jsonify, request
import requests
import random
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route('/api/get-lucky-num', methods=["POST", "GET"])
def response():

    print(len(request.form))
    response = {
        "name" : request.form["name"],
        "email" : request.form["email"],
        "color" : request.form["color"],
        "year" : request.form["year"],
        "lucky number": random.randint(0, 100)
    }
    for item in response:
        if response[item] == "":
            response[item] = ["This field is required"]     
        elif item == "year" or item == "lucky number":
            log = api_getter(response[item])
            logd = log.json()
            for items in logd:
                if items == "text":
                    response[item] = {
                        "fact": logd[items],
                        item: response[item]
                    }
            print(response)

    return render_template("index.html", response=response)

def api_getter(value):
    response = requests.get(f"http://numbersapi.com/{value}?json")
    return response
