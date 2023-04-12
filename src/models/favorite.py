from models.index import db

class Favorite(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet', back_populates='favorite')
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character', back_populates='favorite')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='favorite')
    
    def __init__(self, planet_id=None, character_id=None, user_id=None):
        self.planet_id = planet_id
        self.character_id = character_id
        self.user_id = user_id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
            "user_id": self.user_id
        }