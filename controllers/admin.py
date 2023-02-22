from flask import Blueprint, render_template
from flask_login import login_required

admins=Blueprint("admins",__name__,url_prefix="/administartor",template_folder="../templates/admin")

@admins.route("/")
@login_required
def dashboard():

    return render_template("dashboard.html")
