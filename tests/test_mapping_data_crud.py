from dmdma.applications import mapping_data_crud

def test_incorect_page(client):
    # Redirect for directory not having trailing '/' (incorrect URL)
    assert client.get('/mapping_data_crud').status_code == 308

################################################################################
# ToDo: Look into iteration with @pytest.fixture(scope="function", 
#https://docs.pytest.org/en/6.2.x/fixture.html#fixture-parametrize
#https://stackoverflow.com/questions/68146765/pytest-new-test-for-every-iteration-for-loop-parametrize-fixture
################################################################################
def test_unauthenticated_redirect(client, request):
    
    #grep '@bp.route' dmdma/applications/mapping_data_crud/__init__.py �| cut -d "'" -f 2
    page_list=[
        '/mapping_data_crud/',
        '/mapping_data_crud/entity',
        '/mapping_data_crud/entities',
        '/mapping_data_crud/entity',
        '/mapping_data_crud/entity/1',
        '/mapping_data_crud/entity/1/update',
        '/mapping_data_crud/entity/create',
        '/mapping_data_crud/groups',
        '/mapping_data_crud/group',
        '/mapping_data_crud/group/create',
        '/mapping_data_crud/group/1',
        '/mapping_data_crud/group/1/retrieve',
        '/mapping_data_crud/group/1/update',
        '/mapping_data_crud/group/1/delete',
        '/mapping_data_crud/mappings',
        '/mapping_data_crud/mapping',
        '/mapping_data_crud/mapping/create',
        '/mapping_data_crud/mapping/1',
        '/mapping_data_crud/mapping/1/retrieve',
        '/mapping_data_crud/mapping/1/update',
        '/mapping_data_crud/mapping/1/delete',
        '/mapping_data_crud/reset_db'
        ]

    # Test all pages redirect when not logged in    
    for page in page_list:
        #print("TESTING 302: ", page)
        # Redirect for not logged in account
        assert client.get(page).status_code == 302
    
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    # Test all pages work when logged in
    for page in page_list:
        #print("TESTING 200: ", page)
        assert client.get(page).status_code == 200

################################################################################
# Attempt at dynamic testing for all routes
################################################################################
#def test_all_unauthenticated_redirect(client, app):
#    exemption_list = ['flash',
#                      'redirect',
#                      'render_template',
#                      'url_for',
#                      'with_appcontext'
#                      ]
#    
#    from inspect import getmembers, isfunction
#    functions_list = getmembers(mapping_data_crud, isfunction)
#    functions_to_test_pages=[]
#    print("functions_list: ", functions_list)
#    for function_name in functions_list:
#        this_function_name = function_name[0]
#        if this_function_name not in exemption_list:
#            print("function_name: ", this_function_name)
#            functions_to_test_pages.append(this_function_name)
#    with app.app_context():
#        for function_name in functions_to_test_pages:
#            #assert client.get(url_for('myview')).status_code == 200
#            response = client.get(url_for(function_name))
#            assert response.status_code == 302
################################################################################

def test_homepage(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    #print("user_id: ", session["user_id"])
    
    response = client.get('/mapping_data_crud/')
    assert response.status_code == 200

def test_entities(client):
    # set a user id without going through the login route
    with client.session_transaction() as session:
        session["user_id"] = 1
    # session is saved now
    
    response = client.get('/mapping_data_crud/entity')
    assert response.status_code == 200
    assert 'e1' in str(response.data)

def test_some_objects():
    # Test getting something from the object
    key_name = mapping_data_crud.config.DATABASE_BIND_KEY
    assert key_name == 'mapping_data_crud_db'
    
    test_entity = mapping_data_crud.Entity(reference = 'TEST1', description = 'Test 1')
    assert test_entity.reference == 'TEST1'
    assert test_entity.description == 'Test 1'
    assert test_entity.reference != 'TEST4'

    