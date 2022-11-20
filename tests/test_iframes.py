from dmdma.applications import iframes

def test_incorect_page(client):
    # Redirect for directory not having trailing '/' (incorrect URL)
    assert client.get('/iframes').status_code == 308

def test_homepage_redirect(client):
    # Redirect for not logged in account
    assert client.get('/iframes/').status_code == 302
    assert client.get('/iframes/0').status_code == 302

def test_homepage(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    response = client.get('/iframes/')
    assert response.status_code == 200
    assert 'Welcome to the iFrames page' in str(response.data)
    assert 'Example of including a website.' not in str(response.data)
    assert 'Example of file listing' not in str(response.data)

def test_iframe_page_0(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    response = client.get('/iframes/0')
    assert response.status_code == 200
    assert 'Welcome to the iFrames page' in str(response.data)
    assert 'Example of including a website.' in str(response.data)
    assert 'Example of file listing' not in str(response.data)

def test_iframe_page_2(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    response = client.get('/iframes/2')
    assert response.status_code == 200
    assert 'Welcome to the iFrames page' in str(response.data)
    assert 'Example of including a website.' not in str(response.data)
    assert 'Example of file listing' in str(response.data)
    
def test_iframe_page_dynamic(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    sample_iframe = iframes.IFRAMES_COLLECTION[0]
    response = client.get('/iframes/0')
    assert response.status_code == 200
    assert 'Welcome to the iFrames page' in str(response.data)
    assert sample_iframe.description in str(response.data)
    assert sample_iframe.url in str(response.data)