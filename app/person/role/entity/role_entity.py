from app.db import db
from sqlalchemy.orm import mapper
from app.person.role.model.dto.role_dto import RoleDTO


class RoleEntity(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    person = db.relationship("PersonEntity", back_populates="role")

    def __str__(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def start_mapper():
        # mapper(Person, RolEntity)
        mapper(RoleDTO, RoleEntity)
