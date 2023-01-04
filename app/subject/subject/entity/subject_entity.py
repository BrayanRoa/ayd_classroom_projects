from app.db import db
from sqlalchemy.orm import mapper 
from app.subject.subject.model.suject_dto import SubjectDTO
class SubjectEntity(db.Model):
    
    
    
    __tablename__='subject'
    
    code = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    group = db.relationship('GroupEntity', back_populates='subject')

    def start_mapper():
        mapper(SubjectDTO, SubjectEntity)