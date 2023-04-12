from models.index import db, Favorite

def post_fav_planet(body):
    favorite = Favorite(body['planet_id'], body['character_id'], body['user_id'])
    db.session.add(favorite)
    db.session.commit()
    return favorite.serialize()