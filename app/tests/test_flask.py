import pytest

from backend.server import app
from backend.database.seed import main

@pytest.fixture
def client():
    app.testing = True
    client = app.test_client()
    yield client

@pytest.fixture(autouse=True)
def reset():
    main()

def test_post_new(client):
    # Add a post and see if it increases.
    response = client.get('/api/posts/new')
    data = response.get_json()
    print(data)

    response = client.get('/api/posts/')
    data = response.get_json()
    assert len(data) == 6

def test_posts(client):
    response = client.get('/api/posts/')

    # Plain seed data.
    data = response.get_json()
    assert len(data) == 5

    # Add a post and see if it increases.
    response = client.get('/api/posts/new')
    data = response.get_json()
    print(data)

    response = client.get('/api/posts/')
    data = response.get_json()
    assert len(data) == 6

def test_post_by_author(client):
    data = {
        'author': 'Norma Fisher'
    }

    response = client.get('/api/posts/author', query_string=data)
    data = response.get_json()

    assert data['text'] == 'Whole magazine truth stop whose group.'

def test_time(client):
    response = client.get('/time')

    data = response.get_json()

    assert 'time' in data

def test_factorial(client):
    # Add a post and see if it increases.
    response = client.get('/api/posts/factorial/4')
    data = response.get_json()
    print(data)

    assert data['answer'] == 24
