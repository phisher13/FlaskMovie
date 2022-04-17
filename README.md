# FlaskMovie is a movie forum where you can watch films and have a good mood 🎬
<hr>

## Technology stack: 
- Python
- Flask
- Sqlalchemy
- Postgresql
- Redis
- Celery


<hr/>

## App Features:
- Display list of films;
- Display list of films which filtered by genre;
- Create film director;
- Create/Update/Delete film;
- Login/Registration with JWT;

<hr>

## Installation
- #### Requirements
```python
pip install -r requirements.txt
```
- #### Configuration in .env
````dotenv
SQLALCHEMY_DATABASE_URI=
SQLALCHEMY_TRACK_MODIFICATIONS=
SECRET_KEY=
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
MAIL_SERVER=
MAIL_PORT=
MAIL_USE_TLS=
MAIL_USE_SSL=
MAIL_USERNAME=
MAIL_PASSWORD=
````
- #### Start Celery
````python
celery -A api.celery.worker --loglevel=info
````

- #### Run app
```python
python app.py
```
