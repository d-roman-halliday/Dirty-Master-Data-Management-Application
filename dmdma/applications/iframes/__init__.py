from flask import Blueprint, g, redirect, render_template, url_for
from flask.cli import with_appcontext

from .iframe import iframe_item

# Customise linked iframes here

IFRAMES_COLLECTION=[iframe_item(name = 'example.com',
                                description = 'Example of including a website.',
                                url = 'https://example.com'),
                    iframe_item(name = 'My Blog',
                                description = 'Example of including a website.',
                                url = 'https://datablog.roman-halliday.com'),
                    iframe_item(name = 'Simple File Access',
                                description = 'Example of file listing (via Apache), perhaps a simple solution to distributing that internal weekly CSV report that X department insists on having.',
                                url = 'https://www.roman-halliday.com/js_tools/')
    ]

bp = Blueprint('iframes', __name__, url_prefix='/iframes')
    
@with_appcontext
@bp.route('/')
def home():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    return render_template('iframes/home.html', iframes_collection = IFRAMES_COLLECTION)

#iframe_item

@with_appcontext
@bp.route('/<int:iframe_id>')
def if_item(iframe_id):
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    ifreame_item = IFRAMES_COLLECTION[iframe_id]
    return render_template('iframes/home.html', iframes_collection = IFRAMES_COLLECTION, ifreame_item = ifreame_item)

if __name__ == '__main__':
    pass