from app.person.person.entity.person_entity import PersonEntity
from app.person.person.schema.person_schema import person_schema
from sqlalchemy.exc import NoResultFound,DatabaseError
from flask import jsonify
class ModelUser():
    
    @classmethod
    def login(self, db, mail):
        try:
            data = (
                db.session.query(PersonEntity)
                .filter(PersonEntity.institutional_mail == mail)
                .one()
            )
            # if not PersonEntity.check_password(data.password, password):
            #     return False
            # else:
            return person_schema.dump(data)
        except NoResultFound:
            raise NoResultFound(f'dont exist person with mail {mail}')

