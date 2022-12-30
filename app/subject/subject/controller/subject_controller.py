from flask import Blueprint
from app.subject.subject.service.subject_service import get_all_subjects

subject = Blueprint('subject',__name__)

@subject.route('/')
def get_all():
    return get_all_subjects()