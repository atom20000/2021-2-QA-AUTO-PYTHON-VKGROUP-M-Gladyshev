from parser_log.struct_log import StructLog
from parser_log.exlist import ExList
from mysql_orm.client import MySQLORMClient
from static_var import *
import pytest
import os


def pytest_configure(config):
    client = MySQLORMClient(user=USER_NAME,  password= USER_PASSWORD, db_name=DB_NAME, host=HOST, port=PORT)
    if not hasattr(config, 'workerinput'):
        client.recreate_db()
    client.connect()
    config.client = client


@pytest.fixture(scope='session')
def access_log():
    if os.path.exists(PATH_ACCESS_LOG_FILE):
        list_log = ExList()
        with open(PATH_ACCESS_LOG_FILE,'r') as file:
            for f in file:
                list_oblog = f.replace('"','').rstrip().split()
                list_oblog.insert(3,' '.join([list_oblog.pop(3),list_oblog.pop(3)]))
                list_log.append(StructLog(list_oblog))
        return list_log
    else:
       raise NotImplementedError('Дописать ошибку')

@pytest.fixture(scope='session')
def mysql_orm_client(request):
    client = request.config.client
    yield client
    client.connection.close()