# FLASK MVC WEB BOILERPLATE
A boiler plate code for flask web include following setup:
- flask Model View Controller(MVC) architecture
- flask login
- flask migrate
- flask admin
- flask sql database configuration

### Installations
- to install all the requirements run the command
```
    pip install -r requiremets.txt
```

### Setup and migrate the database
- on main.py file replace with your database connection string
```python
app.config['SQLALCHEMY_DATABASE_URI']="your_database_connection_string"
```
- note this only works with sql databases

- Initialize migrations by running following command
```
    flask db init
```
- set up your first migration 

```
    flask db migrate -m "InitialMigration"
```
- Update the database
```
    flask db upgrade
```

### Create a super/admin user
- to create admin user run following command. replace admin and 1234 with your username and password
```
    python config.py --username admin --password 1234
```

### Run the code
```
    flask run
```
or 
```
    python app.py
```

### Adding models
- add your model to models folder
- also add view to the admin view on config.py file
```python
    admin.add_view( AdminModelView(ModelClassName, db.session))
```

### Adding controller
- in the controllers folder create a new file and initialize with a new blueprint
```python
    from flask import Blueprint, render_template

    blueprintName=Blueprint("blueprintName",__name__,url_prefix="/blueprintName",template_folder="../templates/blueprintName")
     # add routes
    @blueprintName.route("/route")
    # add @login_required decorator for protected routes
    def function_name():
        return render_template("page.html")
``` 
- import and register the controller on the app.py file
```python
    from controllers.controller_name import blueprintName

    app.register_blueprint(blueprintName)
```

### Adding views
- in the template folder create a new folder matching blueprint name
- add a base_name.html for specific blueprint designs like dashboard 
- add html file following jinja2 syntax

### Extend session time
- on main.py file extend the session time by updating this line
```python
    app.permanent_session_lifetime=timedelta(minutes=5) #set more minutes or change to hours
```

### Notes
- user role should be admin for the user to view and edit the admin dashboard models
- The application uses Bootstrap from cdn link in the base html files, you can add it to static folder and change
