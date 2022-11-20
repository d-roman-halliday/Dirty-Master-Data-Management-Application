from dmdma.applications import iframes

def test_incorect_page(client):
    # Redirect for directory not having trailing '/' (incorrect URL)
    assert client.get('/reporting').status_code == 308

def test_homepage_redirect(client):
    # Redirect for not logged in account
    assert client.get('/reporting/').status_code == 302
    assert client.get('/reporting/pivot_sample').status_code == 302
    assert client.get('/reporting/dynamic_sample_1').status_code == 302
    assert client.get('/reporting/dynamic_sample_2').status_code == 302

def test_homepage(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    response = client.get('/reporting/')
    assert response.status_code == 200

def test_pivot_sample(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    response = client.get('/reporting/pivot_sample')
    assert response.status_code == 200

def test_dynamic_sample_1(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    response = client.get('/reporting/dynamic_sample_1')
    assert response.status_code == 200
    #Find a value extracted from the database
    assert 'v3' in str(response.data)