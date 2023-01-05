from flask import Blueprint
from app.subject.project_person.service.project_person_service import get_all_projects_person

project_person = Blueprint('project_person', __name__)

@project_person.route('/')
def get_all():
    return get_all_projects_person()