from flask import Flask
from services.movies import list_of_movies
from services.links import list_of_links
from services.ratings import list_of_ratings
from services.tags import list_of_tags
import json
app = Flask(__name__)

@app.route("/movies")
def movies_json():
    return json.dumps([x.__dict__ for x in list_of_movies])

@app.route("/links")
def links_json():
    return json.dumps([x.__dict__ for x in list_of_links])

@app.route("/ratings")
def ratings_json():
    return json.dumps([x.__dict__ for x in list_of_movies])

@app.route("/tags")
def tags_json():
    return json.dumps([x.__dict__ for x in list_of_movies])

if __name__ == '__app__':
    app.run()