from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import BooleanField, SubmitField, StringField


class JobForm(FlaskForm):
    team_leader = IntegerField('Id руководителя')
    job = StringField('Описание работы')
    work_size = IntegerField('Объем работы в часах')
    collaborators = StringField('Участники работы')
    is_finished = BooleanField('Работа звершена.')
    submit = SubmitField('Добавить')
