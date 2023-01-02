from flask import Blueprint, request
from app.subject.subject.service.subject_service import (
    get_all_subjects, 
    get_all_my_subjects, 
    save_subject)

subject = Blueprint('subject',__name__)

@subject.route('/')
def get_all():
    return get_all_subjects()


@subject.route('/get_my_subjects/<mail>', methods=['GET'])
def get_my_subjects(mail):
    return get_all_my_subjects(mail)


@subject.route('/create_subject', methods=['POST'])
def register_subject():
    data = request.get_json()
    return save_subject(data)