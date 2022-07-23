# Craete distrbution
# https://flask.palletsprojects.com/en/2.1.x/tutorial/deploy/
pip install wheel
python setup.py bdist_wheel

# Copy to server
scp -i ~/<KEY_FILE>.ppk /path/to/local/dist/dmdma-0.1.2-py3-none-any.whl <user>@<host>:/var/www/<site_files_location>/dmdma/.

# Craete venv
cd /var/www/<site_files_location>/dmdma/.

python3 -m venv venv
source venv/bin/activate
python3 --version
pip install --upgrade pip

# Install (or upgrade)
pip install dmdma-0.1.2-py3-none-any.whl
pip install --force-reinstall dmdma-0.1.2-py3-none-any.whl

# configure - app.wsgi

# Restart Apache
sudo systemctl reload apache2
