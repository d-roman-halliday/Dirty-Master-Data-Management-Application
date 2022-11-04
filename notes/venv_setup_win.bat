REM create and configure the virtual environment 
py -m pip install --upgrade pip
py -m pip install virtualenv
py -m virtualenv venv


REM activate the virtual environment 
.\venv\Scripts\activate
 
REM check the python version
python --version
 
REM list all packages installed by default
pip list

REM Install this project (and dependencies) 
pip install -e .

REM setting for cmd
SET FLASK_APP=dmdma
SET FLASK_DEBUG=true
REM SET FLASK_ENV=development

REM setting for powershell
$env:FLASK_APP = "dmdma"
$env:FLASK_DEBUG = true
REM $env:FLASK_ENV = "development"

REM init DB (first run)
flask init-db

REM execute server for dev
flask run

REM deactivate the virtual environment
deactivate