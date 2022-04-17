from flask_restx import Resource, marshal_with, Namespace, fields
from flask import request
from flask_jwt_extended import jwt_required

from api.models.movie import Film, Director
from api.models.user import User

movie = Namespace('movie')

schema = movie.model(
    'Film', {
        'id': fields.Integer(),
        'title': fields.String(),
        'genre': fields.String(enums=['ACTION', 'COMEDY', 'DRAMA', 'HORROR', 'FANTASY']),
        'director': fields.String()
    }
)

schema_dir = movie.model(
    'Director', {
        'id': fields.Integer(),
        'name': fields.String(),
        'surname': fields.String(),
        'film': fields.String(),
    }
)


class Login(Resource):
    def post(self):
        params = request.json
        user = User.authenticate(**params)
        token = user.get_token()

        return {"TOKEN": token}


class Register(Resource):
    def post(self):
        params = request.json
        import api.tasks
        api.tasks.send_email.apply_async(args=[params['email']], countdown=0.5)
        user = User(**params)
        user.save()
        token = user.get_token()

        return {"TOKEN": token}


class MovieApi(Resource):
    @marshal_with(schema)
    def get(self):
        """"
        Get all movies
        """
        films = Film.query.all()

        return films

    @marshal_with(schema)
    @jwt_required()
    def post(self):
        """"
        Create new film
        """
        data = request.json
        new_film = Film(
            title=data.get('title'),
            genre=data.get('genre'),
            director=data.get('director')
        )

        new_film.save()

        return new_film

    @marshal_with(schema)
    @jwt_required()
    def put(self, id):
        """"
        Update film by id
        """
        film = Film.get_by_id(id)
        data = movie.payload
        film.title = data['title']
        film.genre = data['genre']
        film.director = data['director']

        film.update()

        return film

    @marshal_with(schema)
    @jwt_required()
    def delete(self, id):
        """
        Delete film by id
        """
        film = Film.get_by_id(id)
        film.delete()

        return film


class DirectorApi(Resource):
    @marshal_with(schema_dir)
    def get(self):
        """"
        Get all movies
        """
        directors = Director.query.all()

        return directors

    @marshal_with(schema_dir)
    @jwt_required()
    def post(self):
        """"
        Create new film
        """
        data = request.json
        new_dir = Director(
            name=data.get('name'),
            surname=data.get('surname'),
            film=data.get('film')
        )

        new_dir.save()

        return new_dir


movie.add_resource(MovieApi, '/')
movie.add_resource(DirectorApi, '/director')
movie.add_resource(Login, '/login')
movie.add_resource(Register, '/register')
