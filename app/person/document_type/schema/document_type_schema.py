from app.ext import ma
from marshmallow import fields
from app.person.person.schema.person_schema import PersonSchema

class DocumentTypeSchema(ma.Schema):
    id=fields.Integer()
    name=fields.String()
    person=fields.Nested(PersonSchema(only=('names', 'institutional_mail'), many=True))
    
document_type_schema=DocumentTypeSchema()
list_documents_type_schema=DocumentTypeSchema(many=True)