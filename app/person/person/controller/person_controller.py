from flask import Blueprint
from app.person.person.service.person_service import get_all_person 

person = Blueprint('person', __name__)


@person.route('/person', methods=['GET'])
def get_all():
    return get_all_person()