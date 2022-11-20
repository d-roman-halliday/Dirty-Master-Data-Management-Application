# Inspired by: https://www.askpython.com/python-modules/flask/flask-crud-application
# Original objects from existing database using: https://pypi.org/project/sqlacodegen/

from flask_sqlalchemy import SQLAlchemy

from . import config

db = SQLAlchemy()

class Entity(db.Model):
    __tablename__ = 'entities'
    __bind_key__ = config.DATABASE_BIND_KEY

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reference = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, nullable=False, server_default=db.sql.func.now())

    def __init__(self, reference, description = None):
        self.reference = reference
        self.description = description
 
    def __repr__(self):
        return f"{self.id}:{self.reference}"

class EntityGroupMapping(db.Model):
    __tablename__ = 'entity_group_mappings'
    __bind_key__ = config.DATABASE_BIND_KEY

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.ForeignKey("entities.id"), nullable=False)
    group_id = db.Column(db.ForeignKey("groups.id"), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, server_default=db.sql.func.now())
    
    db.UniqueConstraint(entity_id, group_id)
    
    entity = db.relationship("Entity")
    group = db.relationship("Group")

    def __init__(self, entity_id, group_id):
        self.entity_id = entity_id
        self.group_id = group_id
 
    def __repr__(self):
        return f"{self.id}:{self.entity_id}-{self.group_id}"

class Group(db.Model):
    __tablename__ = 'groups'
    __bind_key__ = config.DATABASE_BIND_KEY

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reference = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, nullable=False, server_default=db.sql.func.now())

    def __init__(self, reference, description = None):
        self.reference = reference
        self.description = description
 
    def __repr__(self):
        return f"{self.id}:{self.reference}"

if __name__ == '__main__':
    pass