from base import BaseCase
from models.models import *

class TestOne(BaseCase):
    
    def test_all_count_request(self):
        self.mysql.create_table('CountAllRequest')
        insert_row = CountAllRequest(Count_All_Request=len(self.access_log))
        self.mysql.insert_row(insert_row)
        response = self.mysql.select_all_rows(CountAllRequest)
        assert response[0].Count_All_Request == insert_row.Count_All_Request
