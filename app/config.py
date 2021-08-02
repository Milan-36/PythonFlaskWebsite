"""Flask configuration."""
import os


class Config:
    SECRET_KEY = os.urandom(32)  # to generate secret key
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = 'GDtfDCFYjD'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'