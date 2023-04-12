from models.index import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)
    favorite = db.relationship('Favorite', back_populates='character')

    
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description
        }