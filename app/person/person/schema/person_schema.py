from app.ext import ma
from marshmallow import fields, validate
from marshmallow.exceptions import ValidationError

def validate_email(email):
    if '@ufps.edu.co' not in email:
        raise ValidationError("It is not a valid institutional email")
    
class PersonSchema(ma.Schema):
    institutional_mail = fields.Email(
        validate=validate_email,
        required=True,
    )
    password = fields.String(required=True)
    names = fields.String(required=True)
    lastnames = fields.String(required=True)
    code = unique = fields.String(validate=validate.Length(min=7, max=8))
    document_type_id = fields.Integer(required=True)
    role_id = fields.Integer(required=True)


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True, exclude=["password"])
