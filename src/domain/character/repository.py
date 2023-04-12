from models.index import db, Character

def get_all_characters():
    data = Character.query.all()
    data = list(map(lambda char : char.serialize(), data))
    return data

def get_one_character(id):
    data = Character.query.get(id)
    if data is None:
        return data
    return data.serialize()

def post_character(body):
    character = Character(body['name'], body['description'])
    db.session.add(character)
    db.session.commit()
    return character.serialize()

def delete_character(id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()
    return character.serialize()