from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from celery import Celery

from config import Config
from api.db import db
from api.models.movie import Film, Director
from api.models.user import User
from api.routes import movie


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)
celery = Celery(app)
mail = Mail(app)

# App configuration

api = Api(app)
migrate = Migrate(app, db)


api.add_namespace(movie)
