# Not much change from: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/
# ToDo: Extend this
from dmdma import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

