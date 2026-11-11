from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_hello():
    client = app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b"Default Message"
