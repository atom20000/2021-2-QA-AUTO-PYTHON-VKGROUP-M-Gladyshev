from fixtures import *

@pytest.fixture(scope='session')
def photo_dir():
    photo_dir = os.path.join(os.getcwd(),'photo')
    if os.path.exists(photo_dir):
        shutil.rmtree(photo_dir)
    os.mkdir(photo_dir)
    return photo_dir