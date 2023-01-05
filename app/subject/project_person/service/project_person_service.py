from app.db import db
from flask import jsonify
from app.subject.project_person.entity.project_person_entity import ProjectPersonEntity

def get_all_projects_person():
    data = db.session.query(ProjectPersonEntity).all()
    return jsonify(data)