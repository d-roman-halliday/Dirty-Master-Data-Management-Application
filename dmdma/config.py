"""Flask configuration."""

# Inspired by: https://hackersandslackers.com/configure-flask-applications/

from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config():
    """Base config.""" 
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    ############################################################################
    # Configure Database and binds (allows for multiple independent databases)
    ############################################################################
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dmdma_db2.sqlite'

    SQLALCHEMY_BINDS = {
        'dmdma' : SQLALCHEMY_DATABASE_URI,
        'mapping_data_crud_db' : "sqlite:///mapping_data_crud_db.sqlite"
        }
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

if __name__ == '__main__':
    pass