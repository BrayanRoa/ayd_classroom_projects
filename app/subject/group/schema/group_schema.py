from app.ext import ma
from marshmallow import fields


class GroupSchema(ma.Schema):

    code = fields.Integer()
    name = fields.String()
    number_of_students = fields.Integer()
    subject_id = fields.String()


group_schema = GroupSchema()
list_group_schema = GroupSchema(many=True)
