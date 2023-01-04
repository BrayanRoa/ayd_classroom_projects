from flask import Flask
from .db import db
from app.ext import ma, migrate
from app.person.person.controller.person_controller import person
from app.person.document_type.controller.document_type_controller import document_type
from app.person.role.controller.role_controller import role
from app.auth.controller.auth_controller import auth
from app.subject.subject.controller.subject_controller import subject
from app.subject.group.controller.gruop_controller import group
from app.subject.group_person.controller.group_person_controller import group_person
# from app.subject.subject_person.controller.subject_person_controller import subject_person

prefix = f"/api/v1"

import pymysql
pymysql.install_as_MySQLdb()

def create_app(setting_module):
    app = Flask(__name__)
    
    app.config.from_object(setting_module)
    app.url_map.strict_slashes = False  # *

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)
    #! BLUEPRINTS
    app.register_blueprint(person, url_prefix=f"{prefix}/person")
    app.register_blueprint(document_type, url_prefix=f"{prefix}/document_type")
    app.register_blueprint(role, url_prefix=f"{prefix}/role")
    app.register_blueprint(auth, url_prefix=f"{prefix}/auth")
    app.register_blueprint(subject, url_prefix=f"{prefix}/subject")
    app.register_blueprint(group, url_prefix=f"{prefix}/group")
    app.register_blueprint(group_person, url_prefix=f"{prefix}/group_person")
    # app.register_blueprint(subject_person, url_prefix=f"{prefix}/subject_person")
    return app