from app.db import db
from app.person.person.entity.person_entity import PersonEntity
from app.person.document_type.entity.document_type_entity import DocumentTypeEntity
from app.person.person.schema.person_schema import person_schema, persons_schema
from flask import jsonify
from marshmallow import ValidationError
from app.person.person.model.dto.person_dto import PersonDTO
from sqlalchemy.exc import NoResultFound
from werkzeug.security import generate_password_hash

# ! TODO: 👀 TAMPOCO ESTOY UTILIZANDO EL MODELO PARA NADA
# ! TODO: ⬇️ PREGUNTARLE A SANTIAGO SOBRE ESTO
PersonEntity.start_mapper()


def get_all_person():
    data = db.session.query(PersonEntity).all()
    if not data:
        return {"msg": "There are not persons"}, 404
    result = persons_schema.dump(data)
    return jsonify({"data": result}), 200


# * FIXME: ES UNA COPIA DEL DE ARRIBA ⬆️
def get_teachers():
    data = db.session.query(PersonEntity).filter(PersonEntity.role_id == 1)
    if not data:
        return {"msg": "There are not persons"}, 404
    result = persons_schema.dump(data)
    return jsonify({"data": result}), 200


def save_person(data):
    person = None
    try:
        data['password']=generate_password_hash(data['password'])
        person = person_schema.load(data)
        db.session.add(
            PersonDTO(
                institutional_mail=person["institutional_mail"],
                names=person["names"],
                lastnames=person["lastnames"],
                code=person["code"],
                password=person["password"],
                document_type_id=person["document_type_id"],
                role_id=person["role_id"],
            )
        )
        db.session.commit()
        return jsonify({"data": person}), 201
    except ValidationError as error:
        return jsonify({"error": error.messages}), 400
    except Exception as ex:
        return jsonify({"MySql": ex.args}), 400

# TODO: VER COMO HAGO PARA NO MOSTRAR ALGUNOS CAMPOS EN LA RESPUESTA
def get_person_mail(mail):
    try:
        data = (
            db.session.query(PersonEntity)
            .filter(PersonEntity.institutional_mail == mail)
            .one()
        )
    except NoResultFound:
        return jsonify({"msg": f'There is not person with email {mail}'}), 404
    
    result = person_schema.dump(data)
    return jsonify({"data": result}), 200
