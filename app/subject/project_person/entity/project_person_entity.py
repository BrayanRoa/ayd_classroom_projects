from app.db import db
from sqlalchemy.orm import mapper
from sqlalchemy.schema import ForeignKey

class ProjectPersonEntity(db.Model):
    __tablename__='project_person'
    
    person_id = db.Column(db.String(100), ForeignKey('person.institutional_mail'), primary_key=True)
    project_id = db.Column(db.Integer, ForeignKey('project.code'), primary_key=True)
    #TODO: SERIA BUENO COLOCAR UN ESTADO AQUI PARA SABER SI LA PERSONA TERMINO EL PROYECTO O NO
    # def start_mapper():
    #     mapper(SubjectPersonDTO, SubjectPersonEntity)