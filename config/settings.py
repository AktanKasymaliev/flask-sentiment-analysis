import os

from config.configurations import config

basedir = os.path.abspath(os.path.dirname(__file__))

config()

class Config:
    DEBUG = eval(os.environ.get('FLASK_DEBUG', "True"))
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('FLASK_KEY', 'my-secret-key')

class ProductionConfig(Config):
    DEVELOPMENT = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'