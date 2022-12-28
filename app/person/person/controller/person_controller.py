from flask import Blueprint, request
from app.person.person.service.person_service import get_all_person, save_person

person = Blueprint('person', __name__)


@person.route('/person', methods=['GET'])
def get_all():
    return get_all_person()

@person.route('/create', methods=['POST'])
def create_person():
    person = request.get_json()
    print(person)
    return save_person(person)
    