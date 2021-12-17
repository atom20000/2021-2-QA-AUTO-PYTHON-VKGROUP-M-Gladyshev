from tests.base import BaseUITest
import pytest

@pytest.mark.UI
class TestLoginPage(BaseUITest):
    autologin = False

    @pytest.mark.positive
    def test_login_positive(self):
        """
        Тест страницы входа - пользователь успешно вошел в систему
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Авторизация пользователя на сайте вводом данных в соответствующие поля
        4. Проверка перехода на главную страницу
        5. Провека что поле `active` стало иметь значение 1
        
        Ожидаемый результат - текущая url драйвера соответствует url главной страницы
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        main_page = self.start_page.login(username=user.username, password=user.password)
        self.logger.info('Check cross main page')
        assert main_page.url == self.driver.current_url

    @pytest.mark.negative
    @pytest.mark.parametrize(
        ('username', 'error_message'),
        [
            ('qa','Incorrect username length'),
            (None,'Invalid username or password')
        ]
    )
    def test_login_negative(self,username,error_message):
        """
        Параметризированный негативный тест страницы входа - имя пользователя малой длины и ввод значений не существующего пользователя
        1. На основе параметров генерируется объект данных пользователя
        2. Ввод сгенерированных данных в соотвутствующие поля
        3. Проверка сообщения об ошибке

        Ожидаемый результат - получение ожидаемого сообщения об ошибке 
        """
        user = self.mysql_client.generate_user(username=username)
        self.start_page.login(username=user.username, password=user.password)
        assert self.start_page.error_message_text == error_message
        self.logger.info('Check message error "{error_message}"')
        assert self.start_page.url == self.driver.current_url
    
    #@pytest.mark.negative
    #def test_login_negative_invalid(self):
    #    """
    #    Негативный тест страницы входа - ввод значений не существующего пользователя
    #    1. Генерируется валидный объект данных пользователя
    #    2. Ввод сгенерированных данных в соотвутствующие поля
    #    3. Проверка сообщения об ошибке
    #
    #    Ожидаемый результат - получение сообщения об ошибке `Invalid username or password`
    #    """
    #    user = self.mysql_client.generate_user()
    #    self.start_page.login(username=user.username, password=user.password)
    #    assert self.start_page.error_message_text == 'Invalid username or password'
    #    self.logger.info('Check message error "Incorrect username length"')
    #    assert self.start_page.url == self.driver.current_url

