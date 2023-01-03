from app.ext import ma
from marshmallow import fields, validate
from app.subject.group.schema.group_schema import GroupSchema


class SubjectSchema(ma.Schema):
    
    code= fields.String(required=True, validate=validate.Length(min=7, max=8))
    name= fields.String(required=True, validate=validate.Length(min=3))
    subject_person = fields.Nested('SubjectPersonSchema', many=True)
    group = fields.Nested('GroupSchema', only=('code','name'), many=True)
    
subject_schema=SubjectSchema()
subjects_schema=SubjectSchema(many=True)
    
     
