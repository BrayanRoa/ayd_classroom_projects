from app.db import db
from flask import jsonify
from app.person.document_type.entity.document_type_entity import DocumentTypeEntity
from app.person.person.entity.person_entity import PersonEntity
from app.person.document_type.schema.document_type_schema import list_documents_type_schema

def get_all_documents():
    data = db.session.query(DocumentTypeEntity).all()
    if not data:
        return {"msg":"There are not persons"}, 404
    
    for person in data:
        print(person)
    result = list_documents_type_schema.dump(data)
    return jsonify({'data':result})