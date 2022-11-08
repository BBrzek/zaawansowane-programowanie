from flask import Flask
from services.movies import list_of_movies
import json
app = Flask(__name__)

@app.route("/movies")
def movies_json():
    return json.dumps([x.__dict__ for x in list_of_movies])

@app.route("/links")
def movies_json():
    return json.dumps([x.__dict__ for x in list_of_movies])

@app.route("/ratings")
def movies_json():
    return json.dumps([x.__dict__ for x in list_of_movies])

@app.route("/tags")
def movies_json():
    return json.dumps([x.__dict__ for x in list_of_movies])

if __name__ == '__app__':
    app.run()