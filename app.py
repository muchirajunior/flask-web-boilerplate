from flask import jsonify, render_template
from config import app
from controllers.admin import admins
from controllers.home import home
from controllers.user import users
from flask_login import login_required

app.register_blueprint(home)
app.register_blueprint(admins)
app.register_blueprint(users)


if __name__=="__main__":
    app.run(debug=True,port=5000)