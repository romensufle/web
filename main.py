from flask import Flask, request, url_for, render_template, redirect
from flask_login import login_user

from data import db_session
from api import jobs_api, jobs_api_one
from data.jobs import Jobs
from data.user import User
from forms.login import LoginForm1
from forms.loginform import LoginForm
from forms.register_form import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm1()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('auth.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('auth.html', title='Авторизация', form=form)


@app.route('/login_alert', methods=['GET', 'POST'])
def login_alert():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'успех'


@app.route('/')
def start():
    return render_template('base.html', title='Миссия Колонизация Марса')


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html', title='Миссия Колонизация Марса')


@app.route('/list_prof/<listt>')
def profs(listt):
    lst = ['инженер-исследователь', 'пилот', 'строитель',
           'экзобиолог', 'врач', 'инженер по терраформированию',
           'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
           'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
           'штурман', 'пилот дронов']
    return render_template('prof.html', prof=lst, listype=listt)


@app.route('/index')
def index():
    return render_template('base.html', title='Миссия Колонизация Марса')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/load_foto', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return render_template('load_photo.html')
    elif request.method == 'POST':
        photo = request.files['file']  # получение файла
        with open('static/img/img.jpg', mode='wb') as f:
            f.write(photo.read())
        return render_template('show_photo.html')


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                              <option>7</option>
                                              <option>8</option>
                                              <option>9</option>
                                              <option>10</option>
                                              <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                            <p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    Ссылка с href
  </a>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Кнопка с data-target
  </button>
</p>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    Некоторый заполнитель для компонента сворачивания. Эта панель по умолчанию скрыта, но открывается, когда пользователь активирует соответствующий триггер.
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return f"""{request.form.get('email') +
                    request.form['password'] +
                    request.form['class'] +
                    request.form['file'] +
                    request.form['about'] +
                    request.form['accept'] +
                    request.form['sex']
        }"""


def add_user():
    # связать с формой регистрации
    sess = db_session.create_session()
    user = User()
    user.name = 'Dart'
    user.surname = 'Weider'
    user.age = 71
    user.position = 'canon master'
    user.speciality = "sword master"
    user.address = "module_2"
    user.email = "Chernish@mars.org"
    user.hashed_password = "dart"
    sess.add(user)
    sess.commit()
    sess.close()
    sess = db_session.create_session()
    user = User()
    user.name = 'Buzz'
    user.surname = 'Lightyear'
    user.age = 31
    user.position = 'pilot'
    user.speciality = "pilot"
    user.address = "module_1"
    user.email = "svetik@mars.org"
    user.hashed_password = "buzz"
    sess.add(user)
    sess.commit()
    sess.close()
    sess = db_session.create_session()
    user = User()
    user.name = 'Ridley'
    user.surname = 'Scott'
    user.age = 21
    user.position = 'captain'
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    sess.add(user)
    sess.commit()
    sess.close()


def add_job():
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    sess = db_session.create_session()
    sess.add(job)
    sess.commit()
    sess.close()


@app.route("/logs")
def logs():
    # db_name = input()
    # global_init(db_name)
    # sess = create_session()
    sess = db_session.create_session()
    # user = sess.query(User).filter((User.address == 'module_1'),
    #                                (User.speciality.notlike("%engineer%")),
    #                                (User.position.notlike("%engineer%"))).all()
    jobs = sess.query(Jobs).all()
    return render_template('table_logs.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        if form.password.data != form.password_1.data:
            return render_template('register.html',
                                   form=form, message='Пароли не совпали')

        sess = db_session.create_session()

        if sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   form=form, message='Такой пользователь есть!')

        user = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)

        sess.add(user)
        sess.commit()
        return render_template('register.html',
                               form=form, message='Пользователь зарегестрирован!')
    return render_template('register.html', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(jobs_api_one.blueprint)
    # add_user()
    # add_job()
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
