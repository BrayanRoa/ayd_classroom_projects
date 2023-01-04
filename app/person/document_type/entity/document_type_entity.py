from app.db import db
from sqlalchemy.orm import mapper
from app.person.document_type.model.document_type_dto import DocumentTypeDTO
class DocumentTypeEntity(db.Model):
    __tablename__='document_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    person = db.relationship('PersonEntity', back_populates='document_type')
    
    def start_mapper():
        mapper(DocumentTypeDTO, DocumentTypeEntity)