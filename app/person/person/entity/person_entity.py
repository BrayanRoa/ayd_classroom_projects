from app.db import db
from app.person.document_type.entity.document_type_entity import DocumentTypeEntity
from app.person.role.entity.role_entity import RoleEntity
from sqlalchemy.orm import mapper
from app.person.person.model.dto.person_dto import PersonDTO
from app.person.person.model.person import Person
from werkzeug.security import check_password_hash
class PersonEntity(db.Model):
    __tablename__='person'
    
    institutional_mail=db.Column(db.String(100), primary_key=True)
    # password = db.Column(db.String(250), nullable=False)
    names= db.Column(db.String(30), nullable=False)
    lastnames= db.Column(db.String(30), nullable=False)
    code = db.Column(db.String(8), nullable=False, unique=True)
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_type.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    role= db.relationship('RoleEntity', back_populates='person')
    document_type = db.relationship('DocumentTypeEntity', back_populates="person")
    
    group_person = db.relationship('GroupPersonEntity', back_populates='person')
    subject_person = db.relationship('SubjectPersonEntity', back_populates='person')
    
    def __str__(self):
        return {
            "institutional_mail":self.institutional_mail,
            # "password":self.password,
            "names":self.names,
            "lastnames":self.lastnames,
            "code":self.code,
            "role_code":self.role_code,
            "document_type_id":self.document_type_id,
            "role":self.role
        }
      
    def start_mapper():
        # mapper(Person, PersonEntity)
        mapper(PersonDTO, PersonEntity)
        
    # @classmethod #* CON ESTE DECORADOR NO NECESITO INSTANCIAR LA CLASE
    # def check_password(self, hashed_password, password):
    #     return check_password_hash(hashed_password, password)