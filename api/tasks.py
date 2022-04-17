from flask_mail import Message

from api import celery, mail, app


@celery.task
def send_email(email):
    msg = Message('Welcome Email', sender='overbufer999@gmail.com', recipients=[email])
    msg.body = 'Congratulations! You are successfully registered on FlaskMovie'
    with app.app_context():
        mail.send(msg)
