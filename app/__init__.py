from flask import Flask
from .db import db
from app.ext import ma, migrate
from app.person.person.controller.person_controller import person
from app.person.document_type.controller.document_type_controller import document_type

prefix = f"/api/v1"

def create_app(setting_module):
    app = Flask(__name__)
    
    app.config.from_object(setting_module)
    app.url_map.strict_slashes = False  # *

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)
    app.config['JWT_SECRET_KEY']='Sup3r_s3gura' #! TODO: ESTO TOCA ACOMODARLO
    # app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
    #! BLUEPRINTS
    app.register_blueprint(person, url_prefix=f"{prefix}")
    app.register_blueprint(document_type, url_prefix=f"{prefix}")
    return app