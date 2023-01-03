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
from app.person.person.schema.person_schema import persons_schema
SubjectEntity.start_mapper()


def get_all_subjects():
    data = db.session.query(SubjectEntity).all()
    result = list_subject_groups_schema.dump(data)
    return result


def get_all_my_subjects(mail):
    data = (
        db.session.query(PersonEntity)
        .join(GroupPersonEntity)
        .join(GroupEntity)
        .filter(PersonEntity.institutional_mail == mail)
        .all()
    )
    print(data)
    if not data:
        return {"msg": "You don't have registered subjects yet"}, 404
    # result = [
    #     {"subject": group.subject_id, 
    #      "name_subject": group.subject_id, 
    #      "group": group.name}
    #     for person,union, group in data
    # ]
    result = persons_schema.dump(data)
    return result


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
