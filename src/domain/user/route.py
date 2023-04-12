from flask import request
from models.index import User
import domain.user.controller as Controller


def user_route(app):
    @app.route('/users', methods=['GET'])
    def get_all_users():
        return Controller.get_all_users()

    @app.route('/users/<int:id>', methods=['GET'])
    def get_one_user(id):
        return Controller.get_one_user(id)
    
    @app.route('/users', methods=['POST'])
    def post_user():
        body = request.get_json()
        return Controller.post_user(body)
