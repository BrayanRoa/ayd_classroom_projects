from app.db import db
from app.person.document_type.entity.document_type_entity import DocumentTypeEntity
from app.person.role.entity.role_entity import RoleEntity
from sqlalchemy.orm import mapper
from app.person.person.model.dto.person_dto import PersonDTO

# from app.subject.subject_person.entity.subject_person_entity import SubjectPersonEntity


class PersonEntity(db.Model):
    __tablename__ = "person"

    institutional_mail = db.Column(db.String(100), primary_key=True)
    names = db.Column(db.String(30), nullable=False)
    lastnames = db.Column(db.String(30), nullable=False)
    code = db.Column(db.String(8), nullable=False, unique=True)
    document_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    img = db.Column(db.String(255), nullable=True)

    document_type = db.relationship("DocumentTypeEntity", back_populates="person")
    role = db.relationship("RoleEntity", back_populates="person")

    groups = db.relationship(
        "GroupEntity",
        primaryjoin="and_(PersonEntity.institutional_mail == GroupPersonEntity.person_id, GroupPersonEntity.cancelled==0)",
        secondary="group_person",
        lazy="select",
    )
    
    projects = db.relationship(
        "ProjectEntity",
        secondary='project_person',
        lazy='select',
        viewonly=True
    )

    def __str__(self):
        return str(
            {
                "institutional_mail": self.institutional_mail,
                "names": self.names,
                "lastnames": self.lastnames,
                "code": self.code,
                "role_id": self.role_id,
                "document_type_id": self.document_type_id,
                "role": self.role,
                "groups": self.groups,
            }
        )

    def start_mapper():
        mapper(PersonDTO, PersonEntity)

    # @classmethod #* CON ESTE DECORADOR NO NECESITO INSTANCIAR LA CLASE
    # def check_password(self, hashed_password, password):
    #     return check_password_hash(hashed_password, password)
