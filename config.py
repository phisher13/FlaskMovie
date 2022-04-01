import os

from dotenv import load_dotenv

load_dotenv('.env')


class Config:
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
    CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
