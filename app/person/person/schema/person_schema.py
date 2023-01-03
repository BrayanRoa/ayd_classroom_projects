from app.ext import ma
from marshmallow import fields, validate, post_load
from marshmallow.exceptions import ValidationError
from app.subject.subject_person.schema.subject_person_schema import SubjectPersonSchema
from app.subject.group_person.schema.group_person_schema import GroupPersonSchema

def validate_email(email):
    if '@ufps.edu.co' not in email:
        raise ValidationError("It is not a valid institutional email")
    
class PersonSchema(ma.Schema):
    institutional_mail = fields.Email(
        validate=validate_email,
        required=True,
    )
    # password = fields.String(required=True)
    names = fields.String(required=True)
    lastnames = fields.String(required=True)
    code = fields.String(validate=validate.Length(min=7, max=8))
    document_type_id = fields.Integer(required=True)
    role_id = fields.Integer(required=True)
    subject_person = fields.Nested('SubjectPersonSchema',only=('subject_id', 'cancelled'), many=True)
    # group_person = fields.Nested('GroupPersonSchema',only=('group_id', 'cancelled'), many=True)

    @post_load
    def slugify_name(self, in_data, **kwargs):
        in_data["names"] = in_data["names"].lower().strip()
        in_data["lastnames"] = in_data["lastnames"].lower().strip()
        return in_data


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
