from api.client import API_client
import pytest
import requests
import time

@pytest.mark.API
def test_login(login_session):
    session = login_session
    #import pdb; pdb.set_trace()
    Id_segment = session.post_create_segment('dighj').json()['id']
    #time.sleep(15)
    session.delete_remove_segment(Id_segment=Id_segment)