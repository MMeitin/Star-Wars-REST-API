import domain.planet.repository as Repository
import handle_response as Response

def get_all_planets():
    all_planets = Repository.get_all_planets()
    if all_planets is None:
        return Response.response_error('No hay planetas', 400)
    return all_planets

def get_one_planet(id):
    planet = Repository.get_one_planet(id)
    if planet is None:
        return Response.response_error('No existe este planeta', 400)
    return planet

def post_planet(body):
    if body['name'] is None:
        return Response.response_error("Nombre inexistente", 400)
    return Repository.post_planet(body), 201