from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask.cli import with_appcontext

from . import config

from .models import db as crud_db
from .models import Entity, EntityGroupMapping, Group
from pickle import NONE


bp = Blueprint('mapping_data_crud', __name__, url_prefix='/mapping_data_crud')

# Inspired by
#https://www.askpython.com/python-modules/flask/flask-crud-application

@with_appcontext
@bp.route('/')
def home():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    return render_template('mapping_data_crud/home.html')

################################################################################
# Entity is done in a more monolithic style 
################################################################################
@with_appcontext
@bp.route('/entities')
@bp.route('/entity')
@bp.route('/entity/<int:entity_id>')
@bp.route('/entity/<int:entity_id>/<string:entity_action>', methods = ['GET','POST'])
def entity(entity_id = None, entity_action = 'retrieve'):
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    allowed_actions = ['retrieve','update','delete'] # create handled independently
    error_message = None

    if entity_action not in allowed_actions:
        error_message = 'Unrecognised Action: ' + str(entity_action)

    if entity_id is not None and entity_action == 'retrieve':
        returned_entity = Entity.query.filter_by(id=int(entity_id)).first()
        if returned_entity:
            return render_template('mapping_data_crud/entities.html', individual_entity = returned_entity, retrieve_entity = True)

        error_message = 'Entity not found : ' + str(entity_id)

    if entity_id is not None and entity_action == 'update':
        returned_entity = Entity.query.filter_by(id=int(entity_id)).first()
        if returned_entity:
            if request.method == 'POST':
                returned_entity.reference = request.form['entity_reference']
                returned_entity.description = request.form['entity_description']
                crud_db.session.commit()
                return redirect(url_for('mapping_data_crud.entity', entity_id=returned_entity.id, entity_action='retrieve'))
            
            return render_template('mapping_data_crud/entities.html', individual_entity = returned_entity, update_entity = True)

        error_message = 'Entity not found : ' + str(entity_id)

    if entity_id is not None and entity_action == 'delete':
        returned_entity = Entity.query.filter_by(id=int(entity_id)).first()
        if returned_entity:
            if request.method == 'POST' and request.form['entity_delete_verification'] == "true":
                crud_db.session.delete(returned_entity)
                crud_db.session.commit()
                return redirect(url_for('mapping_data_crud.entity'))

            return render_template('mapping_data_crud/entities.html', individual_entity = returned_entity, delete_entity = True, retrieve_entity = True)

        error_message = 'Entity not found : ' + str(entity_id)
    
    entities = Entity.query.all()
    return render_template('mapping_data_crud/entities.html', entities = entities, error_message = error_message, show_create_btn = True)

@with_appcontext
@bp.route('/entity/create', methods = ['GET','POST'])
def entity_create():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    if request.method == 'GET':
        return render_template('mapping_data_crud/entities.html', create_entity = True)
 
    if request.method == 'POST':
        new_reference = request.form['entity_reference']
        new_description = request.form['entity_description']
        new_entity = Entity(reference=new_reference, description=new_description)
        crud_db.session.add(new_entity)
        crud_db.session.commit()
        
        return redirect(url_for('mapping_data_crud.entity', entity_id=new_entity.id, entity_action='retrieve'))
    
    error_message = 'not yet implemented'
    return render_template('mapping_data_crud/entities.html', error_message = error_message)

################################################################################
# Group is done is a more split out style
################################################################################

@with_appcontext
@bp.route('/groups')
@bp.route('/group')
def group():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    groups = Group.query.all()
    return render_template('mapping_data_crud/group.html', groups = groups)

@with_appcontext
@bp.route('/group/create', methods = ['GET','POST'])
def group_create():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    error_message = None
    
    if request.method == 'GET':
        return render_template('mapping_data_crud/group_create.html')
 
    if request.method == 'POST':
        new_reference = request.form['group_reference']
        new_description = request.form['group_description']
        new_group = Group(reference=new_reference, description=new_description)
        crud_db.session.add(new_group)
        crud_db.session.commit()
        
        return redirect(url_for('mapping_data_crud.group_retrieve', group_id=new_group.id))

    error_message = "Something went wrong"
    return render_template('mapping_data_crud/group.html', error_message = error_message)


@with_appcontext
@bp.route('/group/<int:group_id>')
@bp.route('/group/<int:group_id>/retrieve')
def group_retrieve(group_id):
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    error_message = None
    
    if group_id is not None:
        returned_group = Group.query.filter_by(id=int(group_id)).first()
        if returned_group:
            return render_template('mapping_data_crud/group_retrieve.html', individual_group = returned_group)
    
    error_message = "No group found for ID: " + str(group_id)
    return render_template('mapping_data_crud/group.html', error_message = error_message)

@with_appcontext
@bp.route('/group/<int:group_id>/update', methods = ['GET','POST'])
def group_update(group_id):
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    error_message = None
    
    if group_id is not None:
        returned_group = Group.query.filter_by(id=int(group_id)).first()
        if returned_group:
            if request.method == 'POST':
                returned_group.reference = request.form['group_reference']
                returned_group.description = request.form['group_description']
                crud_db.session.commit()
                return redirect(url_for('mapping_data_crud.group_retrieve', group_id=returned_group.id))
            
            return render_template('mapping_data_crud/group_update.html', individual_group = returned_group)
    
    error_message = "No group found for ID: " + str(group_id)
    return render_template('mapping_data_crud/group.html', error_message = error_message)

@with_appcontext
@bp.route('/group/<int:group_id>/delete', methods = ['GET','POST'])
def group_delete(group_id):
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    error_message = None
    
    if group_id is not None:
        returned_group = Group.query.filter_by(id=int(group_id)).first()
        if returned_group:
            if request.method == 'POST' and request.form['group_delete_verification'] == "true":
                crud_db.session.delete(returned_group)
                crud_db.session.commit()
                return redirect(url_for('mapping_data_crud.group'))
            
            return render_template('mapping_data_crud/group_delete.html', individual_group = returned_group)
    
    error_message = "No group found for ID: " + str(group_id)
    return render_template('mapping_data_crud/group.html', error_message = error_message)

@with_appcontext
@bp.route('/mappings')
@bp.route('/mapping')
def mapping():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    mappings = EntityGroupMapping.query.all()
    return render_template('mapping_data_crud/mapping.html', mappings = mappings)

@with_appcontext
@bp.route('/mapping/create', methods = ['GET','POST'])
def mapping_create():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    error_message = None
    
    if request.method == 'GET':
        entities = Entity.query.all()
        groups = Group.query.all()
        return render_template('mapping_data_crud/mapping_create.html', entities = entities, groups = groups)
 
    if request.method == 'POST':
        new_entity_id = request.form['mapping_entity_id']
        new_group_id = request.form['mapping_group_id']
        new_mapping = EntityGroupMapping(entity_id=new_entity_id, group_id=new_group_id)
        crud_db.session.add(new_mapping)
        crud_db.session.commit()
        
        return redirect(url_for('mapping_data_crud.mapping_retrieve', mapping_id=new_mapping.id))

    error_message = "Something went wrong"
    return render_template('mapping_data_crud/mapping.html', error_message = error_message)

@with_appcontext
@bp.route('/mapping/<int:mapping_id>')
@bp.route('/mapping/<int:mapping_id>/retrieve')
def mapping_retrieve(mapping_id):
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    error_message = None
    
    if mapping_id is not None:
        returned_mapping = EntityGroupMapping.query.filter_by(id=int(mapping_id)).first()
        if returned_mapping:
            return render_template('mapping_data_crud/mapping_retrieve.html', individual_mapping = returned_mapping)
    
    error_message = "No mapping found for ID: " + str(mapping_id)
    return render_template('mapping_data_crud/mapping.html', error_message = error_message)

@with_appcontext
@bp.route('/mapping/<int:mapping_id>/update', methods = ['GET','POST'])
def mapping_update(mapping_id):
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    error_message = None
    
    if mapping_id is not None:
        returned_mapping = EntityGroupMapping.query.filter_by(id=int(mapping_id)).first()
        if returned_mapping:
            if request.method == 'POST':
                returned_mapping.entity_id = request.form['mapping_entity_id']
                returned_mapping.group_id = request.form['mapping_group_id']
                crud_db.session.commit()
                return redirect(url_for('mapping_data_crud.mapping_retrieve', mapping_id=returned_mapping.id))
            
            entities = Entity.query.all()
            groups = Group.query.all()
            return render_template('mapping_data_crud/mapping_update.html', individual_mapping = returned_mapping, groups = groups, entities = entities)
    
    error_message = "No mapping found for ID: " + str(mapping_id)
    return render_template('mapping_data_crud/mapping.html', error_message = error_message)

@with_appcontext
@bp.route('/mapping/<int:mapping_id>/delete', methods = ['GET','POST'])
def mapping_delete(mapping_id):
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    error_message = None
    
    if mapping_id is not None:
        returned_mapping = EntityGroupMapping.query.filter_by(id=int(mapping_id)).first()
        if returned_mapping:
            if request.method == 'POST' and request.form['mapping_delete_verification'] == "true":
                crud_db.session.delete(returned_mapping)
                crud_db.session.commit()
                return redirect(url_for('mapping_data_crud.mapping'))
            
            return render_template('mapping_data_crud/mapping_delete.html', individual_mapping = returned_mapping)
    
    error_message = "No mapping found for ID: " + str(mapping_id)
    return render_template('mapping_data_crud/mapping.html', error_message = error_message)

@with_appcontext
@bp.route('/reset_db')
def reset_db():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    ############################################################################
    # Reset database as required
    ############################################################################
    crud_db.drop_all(config.DATABASE_BIND_KEY)
    crud_db.create_all(config.DATABASE_BIND_KEY)
    
    entity_1 = Entity(reference = 'e1', description = 'D1')
    crud_db.session.add(entity_1)
    crud_db.session.commit()
    
    entity_2 = Entity(reference = 'e2', description = 'D2')
    entity_3 = Entity(reference = 'e3', description = 'D3')
    entity_4 = Entity(reference = 'e4', description = 'D4')
    crud_db.session.add(entity_2)
    crud_db.session.add(entity_3)
    crud_db.session.add(entity_4)
    crud_db.session.commit()
    
    group_1 = Group(reference = 'g1', description = 'GD1')
    group_2 = Group(reference = 'g2', description = 'GD2')
    crud_db.session.add(group_1)
    crud_db.session.add(group_2)
    
    eg_mapping_1 = EntityGroupMapping(entity_id = entity_1.id, group_id = group_1.id)
    crud_db.session.add(eg_mapping_1)
    
    crud_db.session.commit()
    ############################################################################
    # Create HTML Table of tables in database
    ############################################################################
    # Define engine connection (more convoluted using bind references)
    bound_engine = crud_db.engines[config.DATABASE_BIND_KEY]

    # Create and execute query
    show_tables_sql = "SELECT name FROM sqlite_master WHERE type='table';"
    results = bound_engine.execute(show_tables_sql)
    
    # Create HTML Table
    resultset_html = '<table id="exportMe" class="table table-striped table-hover table-sm">'
    resultset_html += '<tr class="thead-dark text-center"><th>Table Name</th></tr>'
    for result_row in results:
        resultset_html += '<tr><td>' + str(result_row[0]) + '</td></tr>'
    resultset_html += '</table>'

    # Render page
    return render_template('mapping_data_crud/reset_db.html', table = resultset_html)
 
if __name__ == '__main__':
    pass