from app.db import db
from sqlalchemy.orm import mapper
from app.subject.group.model.group_dto import GroupDTO
class GroupEntity(db.Model):
    
    __tablename__='group'
        
    code=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(1), nullable=False)
    number_of_students=db.Column(db.Integer, nullable=False)

    subject_id = db.Column(db.String(8), db.ForeignKey('subject.code'))
    subject = db.relationship('SubjectEntity', back_populates="group")
    
    persons = db.relationship("PersonEntity", secondary='group_person', lazy='select', viewonly=True)
    projects = db.relationship('ProjectEntity', back_populates='group')

    def __repr__(self) -> str:
        return f'code: {self.code}, name: {self.name}, subject_id: {self.subject_id}'
    
    def start_mapper():
        mapper(GroupDTO, GroupEntity)    
    