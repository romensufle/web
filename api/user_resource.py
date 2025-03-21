from flask import jsonify
from flask_restful import Resource, abort
from data.user import User
from data import db_session


def abort_if_user_not_found(news_id):
    session = db_session.create_session()
    news = session.query(User).get(news_id)
    if not news:
        abort(404, message=f"User {news_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        sess = db_session.create_session()
        user = sess.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('name', 'surname', 'age')
        )})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        sess = db_session.create_session()
        user = sess.query(User).get(user_id)
        sess.delete(user)
        sess.commit()
        return jsonify({'delete success': user_id})

