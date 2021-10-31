from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'taighekgje mchbvikfdb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db' # change to production.db when ready
    db.init_app(app)

    # Importing views and controllers
    from .views import views
    from .controllers import controllers
    from .models import User

    # Registering views and controllers
    app.register_blueprint(views)
    app.register_blueprint(controllers)

    create_database(db, app)

    return app

def create_database(db, app):
    if not path.exists('webapp/' + 'testing.db'):
        db.create_all(app=app)
