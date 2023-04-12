import domain.character.repository as Repository
import handle_response as Response

def get_all_characters():
    all_characters = Repository.get_all_characters()
    if all_characters is None:
        return Response.response_error('No hay personajes', 400)
    return all_characters

def get_one_character(id):
    character = Repository.get_one_character(id)
    if character is None:
        return Response.response_error('No existe este personaje', 400)
    return character

def post_character(body):
    if body['name'] is None:
        return Response.response_error('Nombre inexistente', 400)
    return Repository.post_character(body), 201

def delete_character(id):
    character = Repository.delete_character(id)
    return character