from flask_login import UserMixin
from main import db

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    username=db.Column(db.String(20),unique=True)
    password=db.Column(db.String(200))
    email=db.Column(db.String(30))

    def __init__(self,name,username,password,email):
        self.name=name
        self.username=username
        self.password=password
        self.email=email