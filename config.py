from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from main import app,db
from models.product import Product
from models.user import User

#declare and initialize login manager for the flask app
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="users.login" #if user is not login redirect to login route

#setup the flask admin page
admin=Admin(app,template_mode="bootstrap4")
admin.add_view( ModelView(User, db.session)) 
# remove this product example model and add your models below
admin.add_view( ModelView(Product, db.session)) 


#create login the decorator
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()