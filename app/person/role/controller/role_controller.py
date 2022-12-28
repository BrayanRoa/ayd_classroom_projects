
from flask import Blueprint
from app.person.role.service.role_service import get_all_rols


role = Blueprint('role', __name__)

@role.route('/role', methods=['GET'])
def get_all():
    return get_all_rols()