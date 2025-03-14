import flask

from data import db_session
from data import jobs
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'get_jobs_one',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/<int:job_id>')
def get_jobs(job_id):
    sess = db_session.create_session()
    data = sess.query(Jobs).get(job_id)
    if not data:
        return flask.jsonify({'error': 'no such id'})
    else:
        return flask.jsonify({
            'job':[
                data.to_dict(only=('id', 'team_leader', 'job'))
            ]
        })