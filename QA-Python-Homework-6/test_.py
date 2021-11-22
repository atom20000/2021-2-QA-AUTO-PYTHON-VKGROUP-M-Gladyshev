from base import BaseCase
from models.models import *
import pytest

class TestOne(BaseCase):
    
    @pytest.mark.SQL
    def test_count_all_request(self):
        self.mysql.create_table('CountAllRequest')
        insert_row = CountAllRequest(Count_All_Request=len(self.access_log))
        self.mysql.insert_row(insert_row)
        response = self.mysql.select_all_rows(CountAllRequest)
        assert response[0] == insert_row

    @pytest.mark.SQL
    def test_count_request_by_type(self):
        self.mysql.create_table('CountRequestByType')
        insert_rows = [CountRequestByType(Type=i[0], Count=i[1]) for i in self.access_log.mapped_list('type_request').ex_count()]
        self.mysql.insert_rows(insert_rows)
        response = self.mysql.select_all_rows(CountRequestByType)
        assert all([i in response for i in insert_rows])
    
    @pytest.mark.SQL
    def test_count_request_by_url(self):
        self.mysql.create_table('CountRequestByUrl')
        insert_rows = [CountRequestByUrl(Url=i[0], Count=i[1]) for i in self.access_log.mapped_list('request_url').ex_count().sorted_list(lambda x : -x[1])[:10]]
        self.mysql.insert_rows(insert_rows)
        response = self.mysql.select_all_rows(CountRequestByUrl)
        assert all([i in response for i in insert_rows])

    @pytest.mark.SQL
    def test_request_by_size_with_error400(self):
        self.mysql.create_table('RequestBySizeWithError400')
        insert_rows = [
            RequestBySizeWithError400(
                Url=getattr(i,"request_url"),
                Status_code=getattr(i,"status_code"),
                Size_request=getattr(i,"size_response"), 
                Ip=getattr(i,"ip_client")
            )
            for i in self.access_log.filter_list('status_code',r'4\d\d').sorted_list(lambda x: -int(x.size_response))[:5]
        ]
        self.mysql.insert_rows(insert_rows)
        response = self.mysql.select_all_rows(RequestBySizeWithError400)
        assert all([i in response for i in insert_rows])
    
    @pytest.mark.SQL
    def test_count_request_by_ip_with_error500(self):
        self.mysql.create_table('CountRequestByIpWithError500')
        insert_rows = [
            CountRequestByIpWithError500(
                Ip=i[0], 
                Count=i[1]
            )
            for i in self.access_log.filter_list('status_code', r'5\d\d').mapped_list('ip_client').ex_count().sorted_list(lambda x : -x[1])[:5]
        ]
        self.mysql.insert_rows(insert_rows)
        response = self.mysql.select_all_rows(CountRequestByIpWithError500)
        assert all([i in response for i in insert_rows])

