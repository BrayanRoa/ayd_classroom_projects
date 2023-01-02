from flask import Blueprint, request
from app.subject.group.service.group_service import (
    get_all_gruops,
    save_group_of_subject
    )

group = Blueprint('group', __name__)


@group.route('/')
def get_all():
    return get_all_gruops()

@group.route('create_group', methods=['POST'])
def register_group():
    data = request.get_json()
    return save_group_of_subject(data)