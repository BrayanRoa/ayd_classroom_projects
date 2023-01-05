from app.db import db
from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from app.person.person.entity.person_entity import PersonEntity
from app.person.person.schema.person_schema import person_schema, persons_schema
from app.person.person.model.dto.person_dto import PersonDTO
# from app.subject.subject_person.entity.subject_person_entity import SubjectPersonEntity
from app.subject.group_person.entity.group_person_entity import GroupPersonEntity
from app.subject.group_person.model.group_person_dto import GroupPersonDTO
from app.person.person.schema.person_subject_group import person_subject_group

# ! TODO: 👀 TAMPOCO ESTOY UTILIZANDO EL MODELO PARA NADA
# ! TODO: ⬇️ PREGUNTARLE A SANTIAGO SOBRE ESTO
PersonEntity.start_mapper()
# SubjectPersonEntity.start_mapper()
GroupPersonEntity.start_mapper()

# * ✅
def get_all_person():
    data = db.session.query(PersonEntity).all()
    return persons_schema.dump(data)


# * ✅
def get_person_mail(mail):
    try:
        data = (
            db.session.query(PersonEntity)
            .filter(PersonEntity.institutional_mail == mail)
            .one()
        )
        return person_schema.dump(data)
    except NoResultFound:
        raise NoResultFound(f"There is not person with email {mail}")


# * ✅
def get_teachers():
    data = db.session.query(PersonEntity).filter(PersonEntity.role_id == 1)
    if not data:
        return {"msg": "There are not persons"}, 404
    result = persons_schema.dump(data)
    return jsonify({"data": result}), 200


# * ✅
def save_person(data):
    person = None
    try:
        person = person_schema.load(data)
        db.session.add(
            PersonDTO(
                institutional_mail=person["institutional_mail"],
                names=person["names"],
                lastnames=person["lastnames"],
                code=person["code"],
                document_type_id=person["document_type_id"],
                role_id=person["role_id"],
                img=person["img"],
            )
        )
        db.session.commit()
        return person
    except ValidationError as error:
        raise ValidationError(error.messages)
    except Exception as ex:
        raise Exception(ex.args)


def register_person_in_course_and_group(data):
    try:
        info_register = person_subject_group.load(data)
        get_person_mail(data["person_id"])
        exist_in_subject = get_person_of_subject(data)
        if exist_in_subject:
            return {"msg": "the person is already registered in the matter"}
        else:
            db.session.add(
                GroupPersonDTO(
                    group_id=info_register['group_id'],
                    person_id=info_register['person_id'],
                    cancelleb=False
                )
            )
            db.session.commit()
            return info_register
    except ValidationError as error:
        return jsonify({"error": error.messages}), 400


def get_person_of_subject(data):
    exist = (
        db.session.query(PersonEntity)
        .filter(PersonEntity.institutional_mail == data["person_id"])
        .first()
    )

    for info in exist.groups:
        if info.code == data["group_id"] and info.subject_id == data["subject_id"]:
            return True
    return False
