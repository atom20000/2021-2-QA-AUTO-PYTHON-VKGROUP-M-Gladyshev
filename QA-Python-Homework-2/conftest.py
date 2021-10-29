from fixtures import *
import os
import shutil
import logging
import allure

@pytest.fixture(scope='function')
def photo_dir(temp_dir):
    photo_dir = os.path.join(temp_dir,'photo')
    #if os.path.exists(photo_dir):
    #    shutil.rmtree(photo_dir)
    return photo_dir

def pytest_configure(config):
    root_path = os.path.abspath(os.path.join(os.getcwd(),'data'))
    if not hasattr(config, 'workerinput'):
        if os.path.exists(root_path):
            shutil.rmtree(root_path)
        os.mkdir(root_path)
        os.mkdir(os.path.join(root_path,'allure'))
    config.root_path = root_path

@pytest.fixture(scope='function')
def temp_dir(request):
    temp_dir = os.path.abspath(os.path.join(request.config.root_path, request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')))
    os.mkdir(temp_dir)
    return temp_dir

@pytest.fixture(scope='function')
def logger(temp_dir):
    #import pdb; pdb.set_trace()
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, "w")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()
    
    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)

