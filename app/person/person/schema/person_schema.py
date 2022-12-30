from app.ext import ma
from marshmallow import fields, validate


class PersonSchema(ma.Schema):
    institutional_mail = fields.Email(
        required=True,
        error_messages={
            "required": "Email is mandatory field.",
            "invalid": "The email is not valid.",
        },
    )
    password = fields.String(required=True)
    names = fields.String(required=True)
    lastnames = fields.String(required=True)
    code = unique = fields.String(validate=validate.Length(min=7, max=8))
    document_type_id = fields.Integer(required=True)
    role_id = fields.Integer(required=True)


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True, exclude=["password"])
