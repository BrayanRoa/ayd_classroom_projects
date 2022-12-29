from flask import Blueprint, request
from app.auth.user.model_user import ModelUser
from app.db import db

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["POST"])
def login():
    return ModelUser.login(db, request.json["mail"], request.json["password"])
