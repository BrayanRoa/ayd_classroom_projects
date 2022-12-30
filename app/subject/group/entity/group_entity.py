from app.db import db

class GroupEntity(db.Model):
    
    __tablename__='group'
        
    code=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(1), nullable=False)
    number_of_students=db.Column(db.Integer, nullable=False)
    
    group_person = db.relationship('GroupPersonEntity', back_populates='group')

    subject_id = db.Column(db.String(8), db.ForeignKey('subject.code'))
    subject = db.relationship('SubjectEntity', back_populates="group")
    
    
    