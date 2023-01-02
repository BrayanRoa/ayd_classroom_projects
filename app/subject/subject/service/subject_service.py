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

SubjectEntity.start_mapper()

def get_all_subjects():
    data = db.session.query(SubjectEntity).all()
    result = list_subject_groups_schema.dump(data)
    return result

def get_all_my_subjects(mail):
    data = (
        db.session.query(PersonEntity, GroupPersonEntity, GroupEntity, SubjectEntity)
        .join(GroupPersonEntity, PersonEntity.institutional_mail == GroupPersonEntity.institutional_mail)
        .join(GroupEntity, GroupPersonEntity.group_id == GroupEntity.code)
        .join(SubjectEntity, GroupEntity.subject_id == SubjectEntity.code)
        .filter(GroupPersonEntity.institutional_mail == mail)
        .all()
        )
    
    result = [{
     'subject':group.subject_id,
     'name_subject':subject.name,
     'group':group.name   
    } for person, union, group, subject in data]
    
    return result


def save_subject(data):
    print(data)
    try:
        subject = subject_schema.load(data)
        db.session.add(SubjectDTO(
            code=subject['code'],
            name=subject['name']
        ))
        db.session.commit()
        return subject
    except ValidationError as error:
        return {'error':error.messages}
    except Exception as error:
        return {'error':error.args}
    