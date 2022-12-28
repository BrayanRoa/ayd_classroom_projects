from app.db import db
from flask import jsonify
from marshmallow import ValidationError
from app.person.role.entity.role_entity import RoleEntity
from app.person.role.schema.role_schema import role_schema, rols_schema
from app.person.role.model.dto.role_dto import RoleDTO

RoleEntity.start_mapper()

def get_all_rols():
    data = db.session.query(RoleEntity).all()
    if not data:
        return {"msg": "There are not rols"}, 404
    result = rols_schema.dump(data)
    return jsonify({"data": result}), 200

def save_role(data):
    role = None
    try:
        role = role_schema.load(data)
        db.session.add(RoleDTO(
            name=role['name']
        ))
        db.session.commit()
        return jsonify({'data':role}), 201
    except ValidationError as error:
        return jsonify({'error':error.messages}), 400
    except Exception as ex:
        return jsonify({'MySql':ex.args}), 400
