from flask import Blueprint, render_template
from models.user import User
users=Blueprint("users",__name__)

@users.route("/login")
def login():

    return render_template("login.html")

@users.route('/register')
def register():

    return render_template('register.html')