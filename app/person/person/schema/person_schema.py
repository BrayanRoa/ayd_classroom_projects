from app.ext import ma
from marshmallow import fields

class PersonSchema(ma.Schema):
    institutional_mail=fields.String()
    password = fields.String()
    names= fields.String()
    lastnames= fields.String()
    code =  unique=fields.String()
    document_type_id = fields.Integer()
   
person_schema=PersonSchema()
persons_schema=PersonSchema(many=True)