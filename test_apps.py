import json

import flask

from apps import app

def test_api_hello():
    response = app.test_client().get('/hello')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['message'] == 'Hello World'

def test_api_ack_without_param():
    response = app.test_client().get('/ack')
    assert response.status_code == 404

def test_api_ack_with_interger_param():
    response = app.test_client().get('/ack/0')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 404
    assert data['message'] == 'Query Param must be a string'

def test_api_ack_with_string_param():
    param = 'test'
    response = app.test_client().get(f'/ack/{param}')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == param.upper()

def test_api_postme_without_data():
    payload = None
    content_type = 'application/json'
    response = app.test_client().post(f'/postme',
        data=json.dumps(payload),
        content_type=content_type
    )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 404
    assert data['message'] == 'No Payload'

def test_api_postme_without_required_data():
    payload = {'bar': 123}
    content_type = 'application/json'
    response = app.test_client().post(f'/postme',
        data=json.dumps(payload),
        content_type=content_type
    )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 404
    assert data['message'] == "'foo' key is missing"

def test_api_postme_with_invalid_content_type():
    payload = {'foo': 123}
    content_type = 'application/text'
    response = app.test_client().post(f'/postme',
        data=json.dumps(payload),
        content_type=content_type
    )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 404
    assert data['message'] == 'Invalid Request'

def test_api_postme_with_valid_request():
    payload = {'foo': 123}
    content_type = 'application/json'
    response = app.test_client().post(f'/postme',
        data=json.dumps(payload),
        content_type=content_type
    )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['message'] == 'Data parsed successfully'
