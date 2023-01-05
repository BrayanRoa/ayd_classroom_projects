
from flask import Blueprint, request
from app.subject.project.service.project_service import get_all_projects, save_project

project = Blueprint('project', __name__)

@project.route('/')
def get_all():
    return get_all_projects()

@project.route('/create_project', methods=['POST'])
def create():
    try:
        data = request.get_json()
        return save_project(data)
    except Exception as error:
        return {'error': error.args}
    
#* TODO: REGISTRAR PERSONA EN PROYECTO - VALIDAR QUE YA NO ESTE EN UNO DE ESA MATERIA