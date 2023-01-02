from app.db import db
from flask import jsonify
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from app.subject.group.entity.group_entity import GroupEntity
from app.subject.group.schema.group_schema import list_group_schema, group_schema
from app.subject.group.model.group_dto import GroupDTO

GroupEntity.start_mapper()

def get_all_gruops():
    data = db.session.query(GroupEntity).all()
    return list_group_schema.dump(data)


def save_group_of_subject(data):
    try:
        group = group_schema.load(data)
        info = group_of_subject(data["subject_id"], data["name"])
        if len(info) > 0:
            return {
                "msg": f"the group {data['name']} already exists for the matter {data['subject_id']}"
            }
        db.session.add(GroupDTO(
            name=group['name'],
            number_of_students=group['number_of_students'],
            subject_id=group['subject_id']
        ))
        db.session.commit()
        return group
    except ValidationError as error:
        return {"error": error.args}


def group_of_subject(code, group):
    try:
        data = (
            db.session.query(GroupEntity)
            .filter(GroupEntity.subject_id == code, GroupEntity.name == group)
            .all()
        )
        return list_group_schema.dump(data)
    except NoResultFound:
        return {"error": NoResultFound.args}
