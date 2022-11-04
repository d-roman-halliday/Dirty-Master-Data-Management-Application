from setuptools import setup

setup(
    name='dmdma',
    # ToDo: Apply models from : https://flask.palletsprojects.com/en/2.1.x/patterns/distribute/?highlight=find_packages
    packages=[
        'dmdma',
        'dmdma.reporting'
    ],
    include_package_data=True,
    install_requires=[
        'flask',
        'bootstrap_flask',
        'pandas',
        'BeautifulSoup4'
    ],
)