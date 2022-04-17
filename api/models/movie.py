from enum import Enum

from api.db import db


class Genres(Enum):
    ACTION = 'action'
    COMEDY = 'comedy'
    DRAMA = 'drama'
    HORROR = 'horror'
    FANTASY = 'fantasy'


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.Enum(Genres), default=None)
    director = db.Column(db.Integer, db.ForeignKey('director.id'), default=None)

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    film = db.relationship('Film')

    def __repr__(self):
        return self.name + ' ' + self.surname

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

