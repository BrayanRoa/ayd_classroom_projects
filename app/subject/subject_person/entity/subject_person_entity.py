from app.db import db

class SubjectPersonEntity(db.Model):
    __tablename__='subject_person'
    
    id=db.Column(db.Integer, primary_key=True)
    cancelled=db.Column(db.Boolean)
    
    institutional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'))
    person = db.relationship('PersonEntity', back_populates="subject_person")

    subject_id = db.Column(db.String(8), db.ForeignKey('subject.code'))
    subject = db.relationship('SubjectEntity', back_populates="subject_person")
    