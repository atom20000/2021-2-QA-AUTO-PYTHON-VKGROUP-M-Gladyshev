
class StructLog():

    def __init__(self,list_obj):
        self.ip_client = list_obj[0]
        self.type_request = list_obj[4]
        self.request_url = list_obj[5]
        self.status_code = list_obj[7]
        self.size_response = list_obj[8]

    def __repr__(self) -> str:
        return f'<StructLog> {self.ip_client}   {self.type_request}  {self.request_url} {self.status_code}  {self.size_response}'