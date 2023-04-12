from models.index import db, Planet

def get_all_planets():
    data = Planet.query.all()
    data = list(map(lambda x : x.serialize(), data))
    return data

def get_one_planet(id):
    data = Planet.query.get(id)
    if data is None:
        return data
    return data.serialize()
    
def post_planet(body):
    planet = Planet(body['name'], body['description'])
    db.session.add(planet)
    db.session.commit()
    return planet.serialize()