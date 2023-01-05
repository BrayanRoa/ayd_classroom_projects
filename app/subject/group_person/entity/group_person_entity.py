from app.db import db
from sqlalchemy.orm import mapper
from app.subject.group_person.model.group_person_dto import GroupPersonDTO

from sqlalchemy import ForeignKey

class GroupPersonEntity(db.Model):
    __tablename__='group_person'
    
    cancelled = db.Column(db.Boolean, default=False)
    person_id = db.Column(db.String(100), ForeignKey('person.institutional_mail'), primary_key=True)
    group_id = db.Column(db.Integer, ForeignKey('group.code'), primary_key=True)
    
    
    def start_mapper():
        mapper(GroupPersonDTO, GroupPersonEntity)