from flask import Blueprint, request, jsonify
from app.subject.subject.service.subject_service import (
    get_all_subjects, 
    get_all_my_subjects, 
    save_subject,
    get_all_person_of_subject_and_group
    )

subject = Blueprint('subject',__name__)

@subject.route('/')
def get_all():
    return get_all_subjects()


@subject.route('/get_my_subjects/<mail>', methods=['GET'])
def get_my_subjects(mail):
    return get_all_my_subjects(mail)

#* ✅
@subject.route('/create_subject', methods=['POST'])
def register_subject():
    data = request.get_json()
    return save_subject(data)

#* ✅
@subject.route('/all_person_of_suject/<code>/<group>', methods=['GET'])
def get_persons_of_subject(code, group):
    try:
        result = get_all_person_of_subject_and_group(code, group)
        return jsonify({"data": result}), 200
    except Exception as error:
        return {'error':error.args}