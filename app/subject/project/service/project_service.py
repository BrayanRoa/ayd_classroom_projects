from app.db import db
from marshmallow import ValidationError
from app.subject.project.schema.project_schema import project_schema, list_projects_schema
from app.subject.project.model.project_dto import ProjectDTO
from app.subject.project.entity.project_entity import ProjectEntity

ProjectEntity.start_mapper()

def get_all_projects():
    projects = db.session.query(ProjectEntity).all()
    return list_projects_schema.dump(projects) 


def save_project(data):
    try:
        project = project_schema.load(data)
        
        db.session.add(ProjectDTO(
            name=project['name'],
            description=project['description'],
            active=False,
            state=project['state'],
            group_id=project['group_id'],
            number_of_students=project['number_of_students']
        ))
        db.session.commit()
        return project
    except ValidationError as error:
        return {'error':error.args},400
    except Exception as error:
        return {'error':error.args}