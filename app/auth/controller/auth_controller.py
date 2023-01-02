from flask import Blueprint, request, jsonify
from app.auth.user.model_user import ModelUser
from app.db import db
from flask_jwt_extended import create_access_token
import datetime

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["POST"])
def login():
    try:
        data = ModelUser.login(db, request.json["mail"])
        # if not data:
        #     return {'error':'password invalid'}
        # else:
        expires = datetime.timedelta(hours=3)
        return {
            "access-token": create_access_token(identity=data['institutional_mail'], expires_delta=expires)
        }, 200
    except Exception as ex:
        return jsonify({'error':ex.args})
