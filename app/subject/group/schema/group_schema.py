from app.ext import ma
from marshmallow import fields, validate


class GroupSchema(ma.Schema):

    code = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=1, max=2))
    number_of_students = fields.Integer()
    subject_id = fields.String(required=True, validate=validate.Length(min=7, max=8))


group_schema = GroupSchema()
list_group_schema = GroupSchema(many=True)
