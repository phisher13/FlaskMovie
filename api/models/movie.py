from enum import Enum

from api import db


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
    director = db.Column(db.Integer, db.ForeignKey('director.id'))

    def __repr__(self):
        return self.title

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.get_or_404(name)


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    film = db.Column(db.relationship('Film', backref='director'))

    def __repr__(self):
        return self.name + ' ' + self.surname
