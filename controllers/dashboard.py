from flask import Blueprint, render_template
from flask_login import login_required

dashboard=Blueprint("dashboard",__name__,url_prefix="/Dashboard",template_folder="../templates/dashboard")

@dashboard.route("/")
@login_required
def index():

    return render_template("dashboard.html")
