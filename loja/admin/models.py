from loja import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(80), unique=False, nullable=False, default='profile.jpg')

    def __init__(self, username, email, password, profile):
       self.username = username
       self.email = email
       self.password = password
       self.profile = profile
        

db.create_all()
