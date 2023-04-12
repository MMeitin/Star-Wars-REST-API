import domain.favorite.repository as Repository
import handle_response as Response

def post_fav_planet(body):
    if body['name'] is None:
        return Response.response_error('Planeta favorito inexistente', 400)
    return Repository.post_fav_planet(body)(body), 201

def post_fav_char(body):
    if body['name'] is None:
        return Response.response_error('Personaje favorito inexistente', 400)
    return Repository.post_fav_char(body), 201

def delete_fav_planet(id):
    character = Repository.delete_fav_planet(id)
    return character

def delete_fav_char(id):
    character = Repository.delete_fav_char(id)
    return character
