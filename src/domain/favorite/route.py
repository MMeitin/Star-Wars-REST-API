from flask import request
from models.index import Favorite
import domain.favorite.controller as Controller

def favorite_route(app):
    
    @app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
    def post_fav_planet():
        body = request.get_json()
        return Controller.post_fav_planet(body)

    @app.route('/favorite/planet/<int:people_id>', methods=['POST'])
    def post_fav_char():
        body = request.get_json()
        return Controller.post_fav_char(body)
    
    @app.route('/favorite/planet/<int:planet_id>',methods=['DELETE'])
    def delete_fav_planet():
        return Controller.delete_fav_planet(id)

    @app.route('/favorite/planet/<int:people_id>',methods=['DELETE'])
    def delete_fav_char():
        return Controller.delete_fav_char(id)