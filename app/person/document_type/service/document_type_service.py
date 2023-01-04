from app.db import db
from flask import jsonify
from marshmallow import ValidationError
from app.person.document_type.entity.document_type_entity import DocumentTypeEntity
from app.person.person.entity.person_entity import PersonEntity
from app.person.document_type.schema.document_type_schema import document_type_schema, list_documents_type_schema
from app.person.document_type.model.document_type_dto import DocumentTypeDTO

DocumentTypeEntity.start_mapper()

def get_all_documents():
    data = db.session.query(DocumentTypeEntity).all()
    if not data:
        return {"msg":"There are not persons"}, 404
    result = list_documents_type_schema.dump(data)
    return jsonify({'data':result})

def save_document(data):
    try:
        document = document_type_schema.load(data)
        db.session.add(DocumentTypeDTO(name=document['name']))
        db.session.commit()
        return document
    except ValidationError as error:
        return {'error':error.args}
    except Exception as error:
        return {'error':error.args}
