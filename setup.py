from setuptools import setup, find_packages

setup(
    name='dmdma',
    # ToDo: Apply models from : https://flask.palletsprojects.com/en/2.1.x/patterns/distribute/?highlight=find_packages
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'bootstrap_flask',
        'pandas',
        'BeautifulSoup4',
        'flask_sqlalchemy'
    ],
)