from flask import jsonify, render_template
from config import app,db
from controllers.user import users
from flask_login import login_required

app.register_blueprint(users)


@app.route('/')
@login_required
def healthCheck():

    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,port=5000)