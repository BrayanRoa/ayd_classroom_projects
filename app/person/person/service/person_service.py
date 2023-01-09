from app.db import db
import json
from flask import jsonify, Response
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from app.person.person.entity.person_entity import PersonEntity
from app.person.person.schema.person_schema import person_schema, persons_schema
from app.person.person.model.dto.person_dto import PersonDTO

# from app.subject.subject_person.entity.subject_person_entity import SubjectPersonEntity
from app.subject.group_person.entity.group_person_entity import GroupPersonEntity
from app.subject.group_person.model.group_person_dto import GroupPersonDTO
from app.person.person.schema.person_subject_group import person_subject_group
from sqlalchemy import func

# ! TODO: 👀 TAMPOCO ESTOY UTILIZANDO EL MODELO PARA NADA
# ! TODO: ⬇️ PREGUNTARLE A SANTIAGO SOBRE ESTO
PersonEntity.start_mapper()
# SubjectPersonEntity.start_mapper()
GroupPersonEntity.start_mapper()

# * ✅
def get_all_person():

    data = db.session.query(PersonEntity).order_by(PersonEntity.code).all()
    return persons_schema.dump(data)
    # data = db.session.query(PersonEntity).all()
    # return persons_schema.dump(data)

    # data = ( #* ESTA FUNCIONA BIEN Y ME HACE UN COUNT
    #     db.session.query(func.count(PersonEntity.institutional_mail))
    #     .filter(PersonEntity.img == "")
    #     .scalar()
    # )
    # return data

    # data = ( #* muestra el correo de la persona y la cantidad de grupos que tenga
    #     db.session.query(
    #         PersonEntity.institutional_mail, func.count(PersonEntity.groups)
    #     )
    #     .group_by(PersonEntity.institutional_mail)
    #     .all()
    # )
    # studenst = [
    #     {'institutional_mail':email, 'num_groups':groups}
    # for email, groups in data]
    # return studenst


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
    data = db.session.query(PersonEntity).filter(PersonEntity.role_id == 1).all()
    if len(data) == 0:
        raise NoResultFound('There are not teachers yet')
    return persons_schema.dump(data)


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
                    group_id=info_register["group_id"],
                    person_id=info_register["person_id"],
                    cancelleb=False,
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
