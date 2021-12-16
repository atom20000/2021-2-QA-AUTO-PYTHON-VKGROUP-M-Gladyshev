from base import BaseUITest
import pytest

class TstUI(BaseUITest):
    @pytest.mark.SQL
    def test(self):
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        mainpage = self.start_page.login(username=user.username, password=user.password)
        assert mainpage.url == mainpage.driver.current_url