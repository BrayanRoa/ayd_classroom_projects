from flask import Blueprint, request, jsonify, g
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.person.person.service.person_service import (
    get_all_person,
    save_person,
    get_teachers,
    get_person_mail,
    register_person_in_course_and_group,
)
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from app.auth.user.user_dto import UserDTO
from sqlalchemy.exc import NoResultFound



person = Blueprint("person", __name__)


# @person.before_request
# def before_request():
#     if verify_jwt_in_request():
#         token = get_jwt()
#         user_info = UserDTO(
#             email=token['sub'],
#             role_id=token['role_id']
#         )
#         g.user_info = user_info.__str__()

#* ✅
@person.route("/", methods=["GET"])
@jwt_required()
def get_all():
    if g.user_info['role_id'] != 1:
        return {'msg':"you don't have the necessary permissions"},401
    
    resp = get_all_person()
    if not resp:
        return {"msg": f"no people registered yet"}, 404
    else:
        return ({"persons": resp}), 200
    
    
#* ✅
@person.route("/<string:mail>", methods=["GET"])
def get_person_by_mail(mail):
    try:
        resp = get_person_mail(mail)
        return jsonify({"person": resp}), 200
    except Exception as error:
        return {"msg": error.args}, 400


# * ✅  
@person.route("/create", methods=["POST"])
def create_person():
    try:
        person = request.get_json()
        resp = save_person(person)
        return jsonify({"person": resp}), 201
    except Exception as error:
        return {"msg": error.args}, 400

#* ✅
@person.route("/teachers", methods=["GET"])
def get_all_teachers():
    try:
        return jsonify({'teachers':get_teachers()}), 200
    except NoResultFound as error:
        return {"Not Found": error.args}, 404        
    except Exception as error:
        return {"msg": error.args}, 400


@person.route("/register_person_in_course", methods=["POST"])
def registerPersonInCourse():
    try:
        data = request.get_json()
        return register_person_in_course_and_group(data)
    except Exception as error:
        return {"error": error.args}
