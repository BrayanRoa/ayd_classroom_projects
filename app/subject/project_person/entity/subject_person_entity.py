# from app.db import db
# from sqlalchemy.orm import mapper
# from sqlalchemy.schema import ForeignKey
# from app.subject.subject_person.model.subject_person_dto import SubjectPersonDTO 


# class SubjectPersonEntity(db.Model):
#     __tablename__='subject_person'
    
#     # person_id = db.Column(db.String(100), ForeignKey('person.institutional_mail'), primary_key=True)
#     subject_id = db.Column(db.String(8), ForeignKey('subject.code'), primary_key=True)
#     cancelled = db.Column(db.Boolean, default=False)
    
#     def start_mapper():
#         mapper(SubjectPersonDTO, SubjectPersonEntity)