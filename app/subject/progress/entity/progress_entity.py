from app.db import db


class ProgressEntity():
    
    __tablename__ = 'progress'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    link = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(30)) #* DEFINIR LOS ESTADOS DE LA ENTREGA
    date = db.Column(db.Date)
    