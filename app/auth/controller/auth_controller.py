from flask import Blueprint, request
from app.auth.user.model_user import ModelUser
from app.db import db
from flask_jwt_extended import create_access_token
import datetime
auth = Blueprint("auth", __name__)


@auth.route("/", methods=["POST"])
def login():
    data = (
        ModelUser.login(
            db, 
            request.json["mail"], 
            request.json["password"])
        )
    expires = datetime.timedelta(hours=3)
    return {'access-token':create_access_token(identity=data, expires_delta=expires)},200
