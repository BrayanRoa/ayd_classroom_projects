from app.ext import ma
from marshmallow import fields
from app.subject.subject.schema.subject_schema import SubjectSchema
class SubjectPersonSchema(ma.Schema):
    
    id=fields.Integer()
    cancelled=fields.Boolean()
    institutional_mail=fields.String()
    subject_id=fields.Integer()
    # subject = fields.Pluck(fields.Nested('SubjectSchema'))
    subject = fields.Pluck("self", "name", many=True)
    
subject_person_schema=SubjectPersonSchema()
subjects_person_schema=SubjectPersonSchema(many=True)
    