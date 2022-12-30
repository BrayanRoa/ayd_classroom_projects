from app.db import db

class SubjectEntity(db.Model):
    
    __tablename__='subject'
    
    code=db.Column(db.String(8), primary_key=True)
    name= db.Column(db.String(30), nullable=False, unique=True)

    subject_person = db.relationship('SubjectPersonEntity', back_populates='subject')
    group = db.relationship('GroupEntity', back_populates='subject')
