from app.ext import ma
from marshmallow import fields

class SubjectGroupSchema(ma.Schema):
    
    code=fields.String()
    name=fields.String()
    group = fields.Nested('GroupSchema', only=('code','name'), many=True)
    

subjec_group_schema = SubjectGroupSchema()
list_subject_groups_schema = SubjectGroupSchema(many=True)     