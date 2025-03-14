from flask_wtf import FlaskForm
from wtforms.fields.simple import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from data import db_session


class LoginForm1(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')