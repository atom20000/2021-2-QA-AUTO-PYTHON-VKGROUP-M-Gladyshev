from api.client import API_client
import os
import shutil
import pytest

@pytest.fixture(scope='session')
def login_session():
    API = API_client()
    API.post_login()
    return API

@pytest.fixture(scope='function')
def photo_dir(temp_dir):
    photo_dir = os.path.join(temp_dir,'photo')
    if not os.path.exists(photo_dir):
       os.mkdir(photo_dir)
    return photo_dir

def pytest_configure(config):
    root_path = os.path.abspath(os.path.join(os.getcwd(),'data'))
    if not hasattr(config, 'workerinput'):
        if os.path.exists(root_path):
            shutil.rmtree(root_path)
        os.mkdir(root_path)
    config.base_temp_dir = root_path

@pytest.fixture(scope='function')
def temp_dir(request):
    temp_dir = os.path.abspath(os.path.join(request.config.base_temp_dir, request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')))
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir