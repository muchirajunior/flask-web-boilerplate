from flask import Blueprint, render_template

home=Blueprint("home",__name__,url_prefix="/",template_folder="../templates/home")

@home.route("/")
def index():
    return render_template("index.html")