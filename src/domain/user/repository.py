from models.index import db, User

def get_all_users():
   data = User.query.all()
   data = list(map(lambda user : user.serialize(), data))
   return data

def get_one_user(id):
    data = User.query.get(id)
    if data is None:
        return data
    return data.serialize()

def post_user(body):
    user = User(body["name"], body["email"])
    db.session.add(user)
    db.session.commit()
    return user.serialize()