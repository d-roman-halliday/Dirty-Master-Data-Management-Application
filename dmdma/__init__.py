from flask import Flask
from flask import render_template

from markupsafe import escape

import os

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

    # Setup DB for internal application
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

    from dmdma import reporting
    app.register_blueprint(reporting.bp)

    return app

if __name__ == '__main__':
    # Create Application
    app = create_app()

    # Run application
    app.run()