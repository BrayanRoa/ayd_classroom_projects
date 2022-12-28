from app.db import db
from app.person.person.entity.person_entity import PersonEntity
from app.person.document_type.entity.document_type_entity import DocumentTypeEntity
from app.person.person.schema.person_schema import person_schema, persons_schema
from flask import jsonify


def get_all_person():
    data = (
        db.session.query(PersonEntity).all()
    )
    if not data:
        return {"msg":"There are not persons"}, 404
    result = persons_schema.dump(data)
    return jsonify({'data':result})
