from flask import Blueprint, request
from app.person.role.service.role_service import get_all_rols, save_role


role = Blueprint("role", __name__)


@role.route("/", methods=["GET"])
def get_all():
    return get_all_rols()


@role.route("/create", methods=["POST"])
def create_role():
    role = request.get_json()
    return save_role(role)
