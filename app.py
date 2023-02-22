from config import app
from controllers.dashboard import dashboard
from controllers.home import home
from controllers.user import users


app.register_blueprint(home)
app.register_blueprint(dashboard)
app.register_blueprint(users)


if __name__=="__main__":
    app.run(debug=True,port=5000)