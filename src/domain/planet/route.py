from flask import request
from models.index import Planet
import domain.planet.controller as Controller

def planet_route(app):
    @app.route('/planets', methods=['GET'])
    def get_all_planets():
        return Controller.get_all_planets()

    @app.route('/planets/<int:id>', methods=['GET'])
    def get_one_planet(id):
        return Controller.get_one_planet(id)

    @app.route('/planets', methods=['POST'])
    def post_planet():
        body = request.get_json()
        return Controller.post_planet(body)