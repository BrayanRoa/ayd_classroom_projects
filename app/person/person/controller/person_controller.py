from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.person.person.service.person_service import (
    get_all_person,
    save_person,
    get_teachers,
    get_person_mail,
    register_person_in_course_and_group,
    get_all_person_of_subject_and_group
)

person = Blueprint("person", __name__)


# @jwt_required()
@person.route("/", methods=["GET"])
def get_all():
    resp = get_all_person()
    if not (resp):
        return {"error": f'There are no people'}, 404
    else:
        return jsonify({"data": resp}), 200


@person.route("/<string:mail>", methods=["GET"])
def get_person_by_mail(mail):
    try:
        resp = get_person_mail(mail)
        return jsonify({"data": resp}), 200
    except Exception as error:
        return {"error": error.args}, 400


@person.route("/create", methods=["POST"])
def create_person():
    try:
        person = request.get_json()
        resp = save_person(person)
        return jsonify({'person':resp}), 201
    except Exception as error:
        return {'error': error.args}, 400


@person.route("/teachers", methods=["GET"])
def get_all_teachers():
    return get_teachers()

@person.route('/all_person_of_suject/<code>/<group>')
def get_person_of_subject(code, group):
    result = get_all_person_of_subject_and_group(code, group)
    if not result:
        return {"error": f'There are no people in subject'}, 404
    return jsonify({'data':result}), 200


@person.route("/register_person_in_course", methods=["POST"])
def registerPersonInCourse():
    try:
        data = request.get_json()
        return register_person_in_course_and_group(data)
    except Exception as error:
        return {'error':error.args}
        
