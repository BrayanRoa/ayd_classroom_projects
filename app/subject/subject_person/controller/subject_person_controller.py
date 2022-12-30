from flask import Blueprint
from app.subject.subject_person.service.subject_person_service import get_all_subject_person

subject_person = Blueprint('subject_person', __name__)

@subject_person.route('/')
def get_all():
    return get_all_subject_person()