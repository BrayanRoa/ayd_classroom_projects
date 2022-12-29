from app.person.person.entity.person_entity import PersonEntity
from sqlalchemy.exc import NoResultFound
from flask import jsonify
class ModelUser:
    
    @classmethod
    def login(self, db, mail, password):
        try:
            data = (
                db.session.query(PersonEntity)
                .filter(PersonEntity.institutional_mail == mail)
                .one()
            )
            valid_password = PersonEntity.check_password(data.password, password)
            if not valid_password:
                return {'error':'password invalid'}, 404
            else:
                return jsonify(data)
        except NoResultFound:
            return {'error':f'dont exist person with mail {mail}'},404
        except Exception as error:
            return {'MySql-Error':error.args}, 400
