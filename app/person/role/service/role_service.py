from app.db import db
from flask import jsonify
from app.person.role.entity.role_entity import RoleEntity
from app.person.role.schema.role_schema import role_schema, rols_schema

def get_all_rols():
    data = db.session.query(RoleEntity).all()
    if not data:
        return {"msg": "There are not rols"}, 404
    result = rols_schema.dump(data)
    return jsonify({"data": result})
