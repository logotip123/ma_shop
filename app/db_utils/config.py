import os
basedir = os.path.abspath(os.path.dirname(__file__))

from .config_ import *

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = "postgres://ma_admin:TheHope@localhost/ma_shop"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "3123123123"


"""App config variables"""
NAME_MAX_LENGTH = 50
PASSWORD_MAX_LENGTH = 50
CATEGORY_MAX_LENGTH = 50
PRODUCT_MAX_LENGTH = 50
