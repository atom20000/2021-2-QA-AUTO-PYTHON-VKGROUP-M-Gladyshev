from api.client import API_client
from utils.Generation_Image import Generation_Image
import pytest
import os
import faker

#@pytest.mark.skip("SKIP")
@pytest.mark.API
def test_create_campaign(login_session:API_client, photo_dir):
    session = login_session
    name_campaign = faker.Faker().bothify(text='test_create_campaign_API ??##?? ?????####')
    url_targ = 'https://studx.ru/'
    Generation_Image().save(os.path.join(photo_dir,f'{name_campaign}.png'))
    response = session.post_create_campaign(name_campaign,url_targ,os.path.join(photo_dir,f'{name_campaign}.png'))
    assert response.status_code == 200 or response.status_code == 204
    Check_campaing = session.get_campaign(Sort_param=f'?_status=active&_id={response.json()["id"]}').json()
    assert Check_campaing['count'] == 1
    assert Check_campaing['items'][0]['id'] == response.json()['id']
    assert session.delete_campaign(response.json()['id']).status_code == 204
    Check_campaing = session.get_campaign(Sort_param=f'?_status=deleted&_id={response.json()["id"]}').json()
    assert Check_campaing['count'] == 1
    assert Check_campaing['items'][0]['id'] == response.json()['id']

#@pytest.mark.skip("SKIP")
@pytest.mark.API
def test_create_segment(login_session:API_client):
    session = login_session
    name_segment = faker.Faker().bothify(text='test_create_segment_API ??##??')
    response = session.post_create_segment(name_segment)
    assert response.status_code == 200 or response.status_code == 204
    #import pdb; pdb.set_trace()
    Check_segment = session.get_segment(response.json()['id'])
    assert Check_segment.status_code != 404
    assert Check_segment.json()['id'] == response.json()['id']
    session.delete_remove_segment(response.json()['id'])

#@pytest.mark.skip("SKIP")
@pytest.mark.API
def test_remove_segment(login_session:API_client):
    session = login_session
    name_segment = faker.Faker().bothify(text='test_create_segment_API ??##??')
    response = session.post_create_segment(name_segment)
    assert response.status_code == 200 or response.status_code == 204
    assert session.delete_remove_segment(response.json()['id']).status_code == 204
    assert session.get_segment(response.json()['id']).status_code == 404

