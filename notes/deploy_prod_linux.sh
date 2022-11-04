################################################################################
# On dev environment: Configure (first time setup)
################################################################################

source ../venv/bin/activate

# https://flask.palletsprojects.com/en/2.1.x/tutorial/deploy/
# Install dependency (first time)
pip install wheel

################################################################################
# On dev environment: Build & Release (push to prod environment)
################################################################################

# Modify release information
# setup.cfg
# version = x.y.z

# Craete distrbution
python setup.py bdist_wheel

# Copy to server
scp -i ~/<KEY_FILE>.ppk /path/to/local/dist/dmdma-0.1.2-py3-none-any.whl <user>@<host>:/var/www/<site_files_location>/dmdma/.


################################################################################
# On prod environment: Configure (first time setup)
################################################################################

cd /var/www/<site_files_location>/dmdma/.

python3 -m venv venv
source venv/bin/activate

python3 --version
pip install --upgrade pip

################################################################################
# On prod environment: Install (or upgrade)
################################################################################

pip install dmdma-0.1.2-py3-none-any.whl
pip install --force-reinstall dmdma-0.1.2-py3-none-any.whl

# configure - app.wsgi (if required at this stage - probably only first time)

# Restart Apache
sudo systemctl reload apache2
