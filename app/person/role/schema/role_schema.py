from app.ext import ma
from marshmallow import fields
from app.person.person.schema.person_schema import PersonSchema

class RolSchema(ma.Schema):
    id=fields.String()
    name= fields.String()
    person=fields.Nested(PersonSchema(only=('names', 'institutional_mail'), many=True))
    
role_schema=RolSchema()
rols_schema=RolSchema(many=True)