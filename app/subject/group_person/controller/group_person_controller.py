from flask import Blueprint
from app.subject.group_person.service.group_person_service import get_all_group_person


group_person = Blueprint('group_person', __name__)

@group_person.route('/')
def get_all():
    return get_all_group_person()