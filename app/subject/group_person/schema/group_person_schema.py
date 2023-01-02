from app.ext import ma
from marshmallow import fields


class GroupPersonSchema(ma.Schema):
    
    id=fields.Integer()
    cancelled=fields.Boolean()
    institutional_mail=fields.String()
    group_id=fields.Integer()
    
group_person_schema=GroupPersonSchema()
groups_person_schema=GroupPersonSchema(many=True)