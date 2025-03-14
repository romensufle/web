import flask

from data import db_session
from data import jobs
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'get_jobs',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    sess = db_session.create_session()
    data = sess.query(Jobs).all()
    d = {}
    for el in data:
        d[el.id] = {
            'team_leader': el.team_leader,
            'job': el.job,
            'work_size': el.work_size,
            'collaborators': el.collaborators,
            'start_date': el.start_date,
            'end_date': el.end_date,
            'is_finshed': el.is_finished
        }
    return flask.jsonify(d)