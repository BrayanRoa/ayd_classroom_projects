from flask import Blueprint
from app.person.document_type.service.document_type_service import get_all_documents

document_type = Blueprint('document_type', __name__)


@document_type.route('/document_type')
def get_all():
    return get_all_documents()
