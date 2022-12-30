from app.db import db

class GroupPersonEntity(db.Model):
    __tablename__='group_person'
    
    id=db.Column(db.Integer, primary_key=True)
    cancelled = db.Column(db.Boolean)
    
    institutional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'))
    person = db.relationship('PersonEntity', back_populates="group_person")

    group_id = db.Column(db.Integer, db.ForeignKey('group.code'))
    group = db.relationship('GroupEntity', back_populates="group_person")
    