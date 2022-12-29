from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.person.person.service.person_service import (
    get_all_person,
    save_person,
    get_teachers,
    get_person_mail
)

person = Blueprint("person", __name__)

@person.route("/", methods=["GET"])
@jwt_required()
def get_all():
    try:
        return get_all_person()
    except Exception as error:
        return {'error':error.args}


@person.route("/create", methods=["POST"])
def create_person():
    person = request.get_json()
    return save_person(person)


@person.route("/teachers", methods=["GET"])
def get_all_teachers():
    return get_teachers()

@person.route('/<string:mail>', methods=['GET'])
def get_person_by_mail(mail):
    return get_person_mail(mail)
