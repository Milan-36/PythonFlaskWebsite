"""Flask configuration."""
import os
import redis


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.urandom(32)  # to generate secret key
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = 'GDtfDCFYjD'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask-Session
    SESSION_TYPE = environ.get('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))