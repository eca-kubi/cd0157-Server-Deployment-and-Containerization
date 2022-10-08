'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'arch@ngel'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjY0NDI1MTMsIm5iZiI6MTY2NTIzMjkxMywiZW1haWwiOiJlY2FrdWJpQGdtYWlsLmNvbSJ9.6wLNEEaqOB1MPh1zQTLEvJhFBiLpXSe5pdXGdrcbp5Y'
EMAIL = 'ecakubi@gmail.com'
PASSWORD = 'runn1ng'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
