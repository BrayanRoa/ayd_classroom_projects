from app.db import db
from sqlalchemy.orm import mapper
from app.subject.project.model.project_dto import ProjectDTO


class ProjectEntity(db.Model):

    __tablename__ = "project"

    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False)
    state = db.Column(db.String(20))
    group_id = db.Column(db.Integer, db.ForeignKey("group.code"))
    number_of_students=db.Column(db.Integer)
    
    group = db.relationship("GroupEntity", back_populates="projects")
    persons = db.relationship("PersonEntity", secondary="project_person", lazy='select')

    def __str__(self) -> str:
        return f"code: {self.code}, name: {self.name}, active: {self.active}"

    def start_mapper():
        mapper(ProjectDTO, ProjectEntity)
