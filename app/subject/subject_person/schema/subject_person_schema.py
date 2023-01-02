from app.ext import ma
from marshmallow import fields

class SubjectPersonSchema(ma.Schema):
    
    id=fields.Integer()
    cancelled=fields.Boolean()
    institutional_mail=fields.String()
    subject_id=fields.Integer()
    
subject_person_schema=SubjectPersonSchema()
subjects_person_schema=SubjectPersonSchema(many=True)
    