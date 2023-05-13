from flask import render_template
from flask import request

from run import app
from webapp.urls import URLPATTERNS
from webapp.utils import get_score_of_sentiment, get_sentiment

@app.route(URLPATTERNS["MAIN_PAGE"], methods=["GET"])
def main_page():
    return render_template("pages/home.html")

@app.route(URLPATTERNS["RESULTS_PAGE"], methods=["POST"])
def results_page():
    text = request.form.get("text")
    if text:
        score = get_score_of_sentiment(text)
        sentiment = get_sentiment(score)
    else: 
        sentiment = None
    return render_template("pages/results.html", sentiment=sentiment)