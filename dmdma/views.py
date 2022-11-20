'''
Created on 23 Jul 2022

@author: davidroman-halliday
'''
#from dmdma import app

import os
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap4

def create_app(test_config=None):
    ############################################################################
    # create and configure the flask app
    ############################################################################
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'dmdma.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Configure bootstrap (used in rendering the pages)
    bootstrap = Bootstrap4(app)

    ############################################################################
    # Configure Database and binds (allows for multiple independent databases)
    ############################################################################
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dmdma_db2.sqlite'
    SQLALCHEMY_BINDS = {}
    SQLALCHEMY_BINDS.update({'dmdma' : SQLALCHEMY_DATABASE_URI}) # Default bind name for application
    
    # Setup DB for internal application (independent database using sqlite3)
    from dmdma import db
    db.init_app(app)

    ############################################################################
    # Configure Sub applications/pages
    ############################################################################
    # Default Page/homepage
    @app.route("/")
    def homepage():
        return render_template('home.html')

    # Blueprints: Authentication
    from dmdma import auth
    app.register_blueprint(auth.bp)

    # Blueprints: iframes (No database)
    from dmdma.applications import iframes
    app.register_blueprint(iframes.bp)

    # Blueprints: Reporting (Database: Uses pandas and own independent database sqlite3)
    from dmdma.applications import reporting
    app.register_blueprint(reporting.bp)
    
    # Blueprints: Mapping Data CRUD (Database: Uses Flask SqlAlchemy and application database [bind])
    from dmdma.applications import mapping_data_crud
    SQLALCHEMY_BINDS.update({mapping_data_crud.config.DATABASE_BIND_KEY : mapping_data_crud.config.DATABASE_URI})
    app.register_blueprint(mapping_data_crud.bp)
    
    ############################################################################
    # Apply database configurations
    ############################################################################
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI    
    app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
    
    # Database for Sub Application: Mapping Data CRUD
    mapping_data_crud.crud_db.init_app(app)
    
    
    return app

