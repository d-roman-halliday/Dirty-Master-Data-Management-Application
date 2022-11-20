################################################################################
# Notes on seting up appropriate venv on mac for dev
################################################################################

# Understand where we are
which python
python --version
pip list

# Manage/change base environments as required (pyenv etc)
# Won't try to document here

# Make sure we are in project working directory

# Venv (seems better on Mac with Eclipse)
python<interpreter version preffered> -m venv venv

# Virtualenv (alternative to venv) - as an option, but didn't work so well for me
pip install virtualenv
virtualenv venv

# Start Venv (whichever method from above)
source venv/bin/activate

# Understand where we are (again)
which python
python --version
pip list

# Install packages & dependencies
pip install --upgrade pip

# pip install -e .
pip install -e Dirty-Master-Data-Management-Application

################################################################################
# Running tests
################################################################################
pip install pytest coverage

coverage run -m pytest

# Verbose output, specific file
coverage run -m pytest -v -s tests/test_mapping_data_crud.py
# Very Verbose output, specific gile
coverage run -m pytest -vv -s tests/test_mapping_data_crud.py
# More output all -
coverage run -m pytest -rA -s tests/test_mapping_data_crud.py

#View coverage of tests
coverage report
# Create detailed report
coverage html
