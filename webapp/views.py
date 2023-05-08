from flask import render_template

from run import app
from webapp.urls import URLPATTERNS

@app.route(URLPATTERNS["MAIN_PAGE"])
def main_page():
    return render_template("pages/home.html")

@app.route(URLPATTERNS["RESULTS_PAGE"])
def results_page():
    return render_template("pages/results.html")