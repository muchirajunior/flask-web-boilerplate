from flask_login import UserMixin
from main import db

class User(db.Model,UserMixin):
    __tablename__="users"
    id:int=db.Column(db.Integer,primary_key=True)
    name:str=db.Column(db.String(50))
    username:str=db.Column(db.String(20),unique=True)
    password:str=db.Column(db.String(200))
    email:str=db.Column(db.String(30))
    role:str=db.Column(db.String(20),default="user") #user/admin
    

    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password