from flask import redirect,request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from main import app,db
from models.product import Product #remove this import sample
from models.user import User

#declare and initialize login manager for the flask app
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="users.login" #if user is not login redirect to login route

#create login the decorator
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

#create a custom model view for protected view
class AdminModelView(ModelView):
    page_size=100
    can_export=True
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role=="admin"
                
    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for("users.restricted"))
        # redirect to login page if user doesn't have access
        return redirect(url_for('users.login', next=request.url))

#setup the flask admin page
admin=Admin(app,template_mode="bootstrap4")
admin.add_view( AdminModelView(User, db.session)) 
# remove this product example model and add your models below
admin.add_view( AdminModelView(Product, db.session)) 


