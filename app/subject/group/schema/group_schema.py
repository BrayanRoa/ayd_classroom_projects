from app.ext import ma
from marshmallow import fields, validate


class GroupSchema(ma.Schema):

    code = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=1, max=2))
    number_of_students = fields.Integer()
    subject_id = fields.String(required=True, validate=validate.Length(min=7, max=8))
    subject = fields.Nested('SubjectSchema', only=('name',))
    persons = fields.Nested('PersonSchema', only=('names', 'lastnames'), many=True)
    projects = fields.Nested('ProjectSchema', only=('name', 'description', 'active'), many=True)
    
#* TODO: ANALIZAR ESTO BIEN
group_schema = GroupSchema(exclude=('projects',))
list_group_schema = GroupSchema(many=True, exclude=('projects',))
list_group_without_persons = GroupSchema(many=True, exclude=('persons',))
