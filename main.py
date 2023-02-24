from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db" #postgresql://username:pass@localhost:5432/database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="ths973ydj28"

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
migrate=Migrate(app,db)

app.permanent_session_lifetime=timedelta(minutes=5) #user session lifetime
