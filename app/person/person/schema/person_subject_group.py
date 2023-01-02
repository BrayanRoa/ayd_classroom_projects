from app.ext import ma
from marshmallow import fields
from app.person.person.schema.person_schema import PersonSchema

#TODO: COLOCAR AQUI LA VALIDACIÓN QUE SEA INSTITUCIONAL

class PersonSubjectGroupSchema(ma.Schema):
    
    institutional_mail=fields.Email()
    subject_id=fields.Integer()
    group_id=fields.Integer()
    
person_subject_group = PersonSubjectGroupSchema()
persons_subject_group = PersonSubjectGroupSchema(many=True)

