from app.subject.group.entity.group_entity import GroupEntity
from app.db import db
from flask import jsonify


def get_all_gruops():
    data = db.session.query(GroupEntity).all()
    return jsonify(data)