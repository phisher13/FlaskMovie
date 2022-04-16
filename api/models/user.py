from datetime import timedelta

from flask_jwt_extended import create_access_token
from passlib.hash import bcrypt


from api.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.username

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.email, expires_delta=expire_delta

        )
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).first()
        if not bcrypt.verify(password, user.password):
            raise Exception('Not user with this password')
        return user

    def save(self):
        db.session.add(self)
        db.session.commit()
