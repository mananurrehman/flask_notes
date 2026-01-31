from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #initialize settings from the config.py file 
    db.init_app(app)
    migrate.init_app(app, db)

    from app import models
    
    from app.routes import bp
    app.register_blueprint(bp)

    return app