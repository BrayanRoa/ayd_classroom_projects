from app.subject.group_person.entity.group_person_entity import GroupPersonEntity
from app.db import db
from flask import jsonify


def get_all_group_person():
    data = db.session.query(GroupPersonEntity).all()
    return jsonify(data)