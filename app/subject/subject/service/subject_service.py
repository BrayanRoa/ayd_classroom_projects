from app.db import db
from app.subject.subject.entity.subject_entity import SubjectEntity
from app.subject.subject.schema.subject_schema import subjects_schema, subject_schema
from app.subject.subject.schema.subject_group_schema import list_subject_groups_schema
from app.person.person.entity.person_entity import PersonEntity
from app.subject.group_person.entity.group_person_entity import GroupPersonEntity
from app.subject.group.entity.group_entity import GroupEntity
from app.subject.subject.model.suject_dto import SubjectDTO
from marshmallow import ValidationError
from flask import jsonify
from app.person.person.schema.person_schema import persons_schema, person_schema
from sqlalchemy import and_
from app.subject.group.schema.group_schema import group_schema
from sqlalchemy.exc import NoResultFound

SubjectEntity.start_mapper()


def get_all_subjects():
    data = db.session.query(SubjectEntity).all()
    result = list_subject_groups_schema.dump(data)
    return result


def get_all_my_subjects(mail):
    data = (
        db.session.query(PersonEntity)
        .filter(PersonEntity.institutional_mail == mail)
        .first()
    )
    if not data:
        return {"msg": "You don't have registered subjects yet"}, 404
    result = person_schema.dump(data)
    return result


# * ✅
def save_subject(data):
    print(data)
    try:
        subject = subject_schema.load(data)
        db.session.add(SubjectDTO(code=subject["code"], name=subject["name"]))
        db.session.commit()
        return subject
    except ValidationError as error:
        return {"error": error.messages}
    except Exception as error:
        return {"error": error.args}


# * ✅
def get_all_person_of_subject_and_group(subject, code_group):
    try:
        exist_subject_ang_group(subject, code_group)
        data = (
            db.session.query(GroupEntity)
            .filter(GroupEntity.code == code_group, GroupEntity.subject_id == subject)
            .first()
        )
        result = group_schema.dump(data)
        return result
    except Exception as error:
        return {"error": error.args}


# * ✅
def exist_subject_ang_group(subject, group):
    try:
        data = (
            db.session.query(GroupEntity)
            .filter(GroupEntity.code == group, GroupEntity.subject_id == subject)
            .one()
        )
        return data
    except NoResultFound:
        raise NoResultFound("check the group or subject")
