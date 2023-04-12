from models.index import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    favorite = db.relationship('Favorite', back_populates='user')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "email": self.email,
        }