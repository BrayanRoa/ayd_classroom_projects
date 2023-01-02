from app.ext import ma
from marshmallow import fields
from app.subject.subject_person.schema.subject_person_schema import SubjectPersonSchema
from app.subject.group.schema.group_schema import GroupSchema


class SubjectSchema(ma.Schema):
    
    code= fields.String()
    name= fields.String()
    subject_person = fields.Nested('SubjectPersonSchema', many=True)
    group = fields.Nested('GroupSchema', only=('code','name'), many=True)
    
    
subject_schema=SubjectSchema()
subjects_schema=SubjectSchema(many=True)
    
     
