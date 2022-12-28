from flask import Blueprint

auth = Blueprint('auth', __name__)

# * TODO: REALIZAR EL LOGIN GENERANDO EL TOKEN
@auth.route('/', methods=['POST'])
def login():
    pass