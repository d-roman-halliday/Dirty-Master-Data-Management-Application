from setuptools import setup

setup(
    name='dmdma',
    packages=['dmdma'],
    include_package_data=True,
    install_requires=[
        'flask',
        'bootstrap_flask',
        'pandas',
        'BeautifulSoup4'
    ],
)