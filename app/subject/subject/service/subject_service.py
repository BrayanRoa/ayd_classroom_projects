from app.db import db
from app.subject.subject.entity.subject_entity import SubjectEntity
from flask import jsonify

def get_all_subjects():
    data = db.session.query(SubjectEntity).all()
    return jsonify(data)