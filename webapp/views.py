from flask import url_for

from run import app

@app.route("/")
def main_page():
    return "<p>Hello, World!</p>"