from mysql_orm.client import MySQLORMClient
import pytest


class BaseCase():

    @pytest.fixture(scope='function',autouse=True)
    def setup(self,access_log, mysql_orm_client):
        self.access_log = access_log
        self.mysql : MySQLORMClient = mysql_orm_client