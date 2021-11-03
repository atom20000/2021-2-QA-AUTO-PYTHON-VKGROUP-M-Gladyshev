import pytest


import pytest
from api.client import API_client

@pytest.fixture(scope='session')
def login_session():
    API = API_client()
    API.post_login()
    return API