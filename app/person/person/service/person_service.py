from app.db import db
from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from app.person.person.entity.person_entity import PersonEntity
from app.person.person.schema.person_schema import person_schema, persons_schema
from app.person.person.model.dto.person_dto import PersonDTO
from app.subject.subject_person.entity.subject_person_entity import SubjectPersonEntity
from app.subject.subject.entity.subject_entity import SubjectEntity
from app.subject.group.entity.group_entity import GroupEntity
from app.subject.group_person.entity.group_person_entity import GroupPersonEntity

from app.subject.subject_person.schema.subject_person_schema import (
    subject_person_schema,
)
from app.subject.subject_person.model.subject_person_dto import SubjectPersonDTO
from app.subject.group_person.model.group_person_dto import GroupPersonDTO


from app.person.person.schema.person_subject_group import person_subject_group
from app.subject.subject.schema.subject_schema import subject_schema, subjects_schema

# ! TODO: 👀 TAMPOCO ESTOY UTILIZANDO EL MODELO PARA NADA
# ! TODO: ⬇️ PREGUNTARLE A SANTIAGO SOBRE ESTO
PersonEntity.start_mapper()
SubjectPersonEntity.start_mapper()
GroupPersonEntity.start_mapper()


def get_all_person():
    data = db.session.query(PersonEntity).all()
    return persons_schema.dump(data)


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


def get_teachers():
    data = db.session.query(PersonEntity).filter(PersonEntity.role_id == 1)
    if not data:
        return {"msg": "There are not persons"}, 404
    result = persons_schema.dump(data)
    return jsonify({"data": result}), 200


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
        get_person_mail(data["institutional_mail"])
        exist_in_subject = get_person_of_seject("one", data)
        if len(exist_in_subject) != 0:
            return {"msg": "the person is already registered in the matter"}
        else:
            db.session.add(
                SubjectPersonDTO(
                    subject_id=info_register["subject_id"],
                    institutional_mail=info_register["institutional_mail"],
                )
            )
            db.session.commit()
            db.session.add(
                GroupPersonDTO(
                    institutional_mail=info_register["institutional_mail"],
                    group_id=info_register["group_id"],
                )
            )
            db.session.commit()
            return info_register
    except ValidationError as error:
        return jsonify({"error": error.messages}), 400


# * ESTA LISTA LA VERIAN LOS DOCENTES
def get_all_person_of_subject_and_group(code, code_group):
    try:
        option = {"query": "all", "subject_code": code, "group": code_group}
        person = get_person_of_seject("all", option)
        result = []
        for student, a, b, c, group in person:
            result.append(
                {
                    "names": student.names,
                    "lastnames": student.lastnames,
                    "mail": student.institutional_mail,
                    "cancelled": a.cancelled,
                },
            )
        return result
    except NoResultFound:
        raise NoResultFound(f"There is not person with email")


def get_person_of_seject(option, data):
    if option == "one":
        exist_in_subject = (
            db.session.query(
                PersonEntity,
                SubjectPersonEntity,
                SubjectEntity,
                GroupPersonEntity,
                GroupEntity,
            )
            .join(
                SubjectPersonEntity,
                SubjectPersonEntity.institutional_mail
                == PersonEntity.institutional_mail,
            )
            .join(SubjectEntity, SubjectPersonEntity.subject_id == SubjectEntity.code)
            .join(
                GroupPersonEntity,
                GroupPersonEntity.institutional_mail == PersonEntity.institutional_mail,
            )
            .join(GroupEntity, GroupPersonEntity.group_id == GroupEntity.code)
            .filter(
                SubjectEntity.code == data["subject_id"],
                GroupEntity.code == data["group_id"],
                PersonEntity.institutional_mail == data["institutional_mail"],
            )
            .all()
        )
        return exist_in_subject
    else:
        exist_in_subject = (
            db.session.query(
                PersonEntity,
                SubjectPersonEntity,
                SubjectEntity,
                GroupPersonEntity,
                GroupEntity,
            )
            .join(
                SubjectPersonEntity,
                SubjectPersonEntity.institutional_mail
                == PersonEntity.institutional_mail,
            )
            .join(SubjectEntity, SubjectPersonEntity.subject_id == SubjectEntity.code)
            .join(
                GroupPersonEntity,
                GroupPersonEntity.institutional_mail == PersonEntity.institutional_mail,
            )
            .join(GroupEntity, GroupPersonEntity.group_id == GroupEntity.code)
            .filter(
                SubjectEntity.code == option["subject_code"],
                GroupEntity.code == option["group"],
            )
            .all()
        )
        return exist_in_subject
