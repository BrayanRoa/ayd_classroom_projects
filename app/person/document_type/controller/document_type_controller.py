from flask import Blueprint, request
from app.person.document_type.service.document_type_service import (
    get_all_documents,
    save_document
    )

document_type = Blueprint('document_type', __name__)


@document_type.route('/')
def get_all():
    return get_all_documents()

@document_type.route('/create', methods=['POST'])
def create():
    try:
        data = request.get_json()
        return save_document(data)
    except Exception as error:
        return {'error':error.args}
