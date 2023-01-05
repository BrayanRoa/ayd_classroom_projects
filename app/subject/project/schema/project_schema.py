from app.ext import ma
from marshmallow import fields, post_load



class ProjectSchema(ma.Schema):
    
    code = fields.Integer()
    name = fields.String()
    description = fields.String()
    active = fields.Boolean()
    state = fields.String() #* A ESTE COLOCARLE UN CONJUNTO DE VALORES PERMITIDOS
    group_id = fields.Integer()
    
    persons = fields.Nested('PersonSchema', only=('names', 'lastnames'), many=True)
    group = fields.Nested('GroupSchema', only=('name','subject'))
    
    @post_load
    def slugify_name(self, in_data, **kwargs):
        in_data["name"] = in_data["name"].lower().strip()
        in_data["description"] = in_data["description"].lower().strip()
        return in_data
    
project_schema = ProjectSchema()
list_projects_schema = ProjectSchema(many=True)