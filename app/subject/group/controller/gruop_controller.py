from flask import Blueprint
from app.subject.group.service.group_service import get_all_gruops


group = Blueprint('group', __name__)


@group.route('/')
def get_all():
    return get_all_gruops()