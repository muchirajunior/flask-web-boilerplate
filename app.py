from config import app
from controllers.home import home
from controllers.user import users

#register blueprints
app.register_blueprint(home)
app.register_blueprint(users)

# uncomment this to run 

# if __name__=="__main__":
#     app.run(debug=True,port=5000)