import domain.user.repository as Repository
import handle_response as Response

def get_all_users():
    all_users = Repository.get_all_users()
    if all_users is None:
        return Response.response_error('No hay usuarios', 400)
        
    return all_users

def get_one_user(id):
    user = Repository.get_one_user(id)
    if user is None:
        return Response.response_error('Usuario no encontrado', 401)
    
    return user

def post_user(body):
    if body['email'] is None:
        return Response.response_error('Email inexistente', 400)
    if body['name'] is None:
        return Response.response_error('Nombre inexistente', 400)

    return Repository.post_user(body), 201