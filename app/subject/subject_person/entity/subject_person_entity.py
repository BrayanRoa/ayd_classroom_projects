from app.db import db
from sqlalchemy.orm import mapper
from app.subject.subject_person.model.subject_person_dto import SubjectPersonDTO 


class SubjectPersonEntity(db.Model):
    __tablename__='subject_person'
    
    id=db.Column(db.Integer, primary_key=True)
    cancelled=db.Column(db.Boolean, default=False)
    
    institutional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'))
    person = db.relationship('PersonEntity', back_populates="subject_person")

    subject_id = db.Column(db.String(8), db.ForeignKey('subject.code'))
    subject = db.relationship('SubjectEntity', back_populates="subject_person")
    
    
    def start_mapper():
        mapper(SubjectPersonDTO, SubjectPersonEntity)