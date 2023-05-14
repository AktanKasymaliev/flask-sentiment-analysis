from flask import Flask

from config.settings import Config


app = Flask(__name__)
app.config.from_object(Config)

import webapp.views