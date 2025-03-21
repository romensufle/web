from xml.sax import parse

from flask import jsonify
from flask_restful import Resource, abort, reqparse
from data.user import User
from data import db_session


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'name', 'surname', 'position')) for item in users]})

    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            position=args['spetiality'],
            address=args['address'],
            email=args['email']
        )
        user.set_password(args['hashed_password'])
        session.add(user)
        session.commit()
        session.close()
        return jsonify({'user': 'ok'})

