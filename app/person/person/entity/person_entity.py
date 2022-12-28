from app.db import db
from app.person.document_type.entity.document_type_entity import DocumentTypeEntity

class PersonEntity(db.Model):
    __tablename__='person'
    
    institutional_mail=db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(250), nullable=False)
    names= db.Column(db.String(30), nullable=False)
    lastnames= db.Column(db.String(30), nullable=False)
    code = db.Column(db.String(8), nullable=False, unique=True)
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_type.id'))
    document_type = db.relationship('DocumentTypeEntity', back_populates="person")
    
    def __str__(self):
        return {
            "institutional_mail":self.institutional_mail,
            "password":self.password,
            "names":self.names,
            "lastnames":self.lastnames,
            "code":self.code,
            "role_code":self.role_code,
            "document_type_id":self.document_type_id,
            # "document_type":self.document_type
        }