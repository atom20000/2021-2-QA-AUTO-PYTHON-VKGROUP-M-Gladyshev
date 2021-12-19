from tests.base import BaseUITest
from pages.main_page import MainPage
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
            ('qa'*9,'Incorrect username length'),
            (None,'Invalid username or password')
        ]
    )
    def test_login_negative(self,username,error_message):
        """
        Параметризированный негативный тест страницы входа - имя пользователя невалидной длины и ввод значений не существующего пользователя
        1. С параметром `username` генерируется объект данных пользователя
        2. Ввод сгенерированных данных в соотвутствующие поля
        3. Проверка сообщения об ошибке

        Ожидаемый результат - `error_message`
        """
        user = self.mysql_client.generate_user(username=username)
        self.start_page.login(username=user.username, password=user.password)
        assert self.start_page.error_message_text == error_message
        self.logger.info(f'Check message error "{error_message}"')
        assert self.start_page.url == self.driver.current_url

    @pytest.mark.positive
    def test_go_to_registration(self):
        """
        Тест страницы входа - переход на страницу регистрации
        1. Нажатие на кнопку с регистрацией
        2. Проверка адреса страницы

        Ожидаем результат - текущийй url страницы соответствует адресу страницы регистрации
        """
        registration_page = self.start_page.go_to_registration()
        assert registration_page.url == self.driver.current_url

@pytest.mark.UI
class TestRegistrationPage(BaseUITest):
    
    autologin = False

    @pytest.mark.positive
    def test_registration(self):
        """
        Тест страницы регистрации - пользователь успешно зарегеистрировался и вошел в систему
        1. Генерируется валидный объект данных пользователя
        2. Регистрация пользователя на сайте вводом данных в соответствующие поля и принять условия
        3. Проверка перехода на главную страницу
        4. Проверить зарегистрированного пользователя в БД

        Ожидаемый результат - текущая url драйвера соответствует url главной страницы
        """
        user = self.mysql_client.generate_user()
        registration_page = self.start_page.go_to_registration()
        main_page = registration_page.registration(
            username=user.username, 
            email=user.email, 
            password=user.password, 
            repassword=user.password)
        assert main_page.url == self.driver.current_url
        assert self.mysql_client.select_user(user.username)

    @pytest.mark.Bug
    @pytest.mark.negative
    def test_negative_registration_russian_text(self):
        """
        Баг. Негативный тест страницы регистрации - имя пользователя на русском языке
        1. С параметром `багбаг` генерируется объект данных пользователя
        2. Регистрация пользователя на сайте вводом данных в соответствующие поля и принять условия
        3. Проверка сообщения об ошибке
        4. Провека текущего адреса

        Ожидаемый результат - текущая url драйвера соответствует url главной страницы
        """
        page = self._registration(username='багбаг')
        assert page.error_message_text == 'Internal Server Error'
        assert MainPage.url == self.driver.current_url

    @pytest.mark.negative
    @pytest.mark.parametrize(
        ('username', 'error_message'),
        [
            ('qa','Incorrect username length'),
            ('qa'*9,'Incorrect username length')
        ]
    )
    def test_negative_registration_invalid_username(self,username,error_message):
        """
        Параметризированный негативный тест страницы регистрации - имя пользователя невалидной длины
        1. С параметром `username` генерируется объект данных пользователя
        2. Ввод сгенерированных данных в соотвутствующие поля
        3. Проверка сообщения об ошибке
        4. Провека текущего адреса

        Ожидаемый результат - `error_message`
        """
        page = self._registration(username=username)
        assert page.error_message_text == error_message
        assert page.url == self.driver.current_url

    @pytest.mark.negative
    def test_negative_registration_invalid_password(self):
        """
        Негативный тест страницы регистрации - пароль пользователя невалидной длины
        1. С параметром `password` генерируется объект данных пользователя
        2. Ввод сгенерированных данных в соотвутствующие поля
        3. Проверка сообщения об ошибке
        4. Провека текущего адреса

        Ожидаемый результат - 'Incorrect password length'
        """
        page = self._registration(password='qa'*128)
        assert page.error_message_text == 'Internal Server Error'
        assert page.url == self.driver.current_url

    @pytest.mark.negative
    @pytest.mark.parametrize(
        ('email', 'error_message'),
        [
            ('qa','Incorrect email length'),
            ('qa'*33,'Incorrect email length'),
            ('@studx.ru', 'Invalid email address'),
            ('soon@studx,ru.ru', 'Invalid email address')
        ]
    )
    def test_negative_registration_invalid_email(self,email,error_message):
        """
        Параметризированный негативный тест страницы регистрации - почта пользователя невалидна
        1. С параметром `email` генерируется объект данных пользователя
        2. Ввод сгенерированных данных в соотвутствующие поля
        3. Проверка сообщения об ошибке
        4. Провека текущего адреса

        Ожидаемый результат - `error_message`
        """
        page = self._registration(email=email)
        assert page.error_message_text == error_message
        assert page.url == self.driver.current_url
    
    @pytest.mark.negative
    def test_negative_registration_invalid_repassword(self):
        """
        Негативный тест страницы регистрации - повтор пароля пользователя невалидный
        1. С параметрами `passwor` и `repassword` генерируется объект данных пользователя
        2. Ввод сгенерированных данных в соотвутствующие поля
        3. Проверка сообщения об ошибке
        4. Провека текущего адреса

        Ожидаемый результат - 'Passwords must match'
        """
        page = self._registration(repassword='1234',password='12')
        assert page.error_message_text == 'Passwords must match'
        assert page.url == self.driver.current_url
    
    @pytest.mark.negative
    def test_negative_registration_with_exist_email(self):
        """
        Негативный тест страницы регистрации - создание пользователя с уже зарегистрированной почтой
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. С параметром `email` генерируется объект данных пользователя
        4. Ввод сгенерированных данных в соотвутствующие поля
        5. Проверка сообщения об ошибке
        6. Провека текущего адреса

        Ожидаемый результат - 'Internal Server Error'
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        page = self._registration(email=user.email)
        assert page.error_message_text == 'Internal Server Error'
        assert page.url == self.driver.current_url

    @pytest.mark.negative
    def test_negative_reregistration_exist_user(self):
        """
        Негативный тест страницы регистрации - повторная регистрация существующего пользователя 
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Ввод сгенерированных данных в соотвутствующие поля
        4. Проверка сообщения об ошибке
        5. Провека текущего адреса

        Ожидаемый результат - 'User already exist'
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        registration_page = self.start_page.go_to_registration()
        page = registration_page.registration(
            username=user.username, 
            email=user.email, 
            password=user.password, 
            repassword=user.password)
        assert page.error_message_text == 'User already exist'
        assert page.url == self.driver.current_url

    @pytest.mark.negative
    def test_negative_registration_dont_accept(self):
        """
        Негативный тест страницы регистрации - не приняты условия соглашения  пользователя 
        1. Генерируется валидный объект данных пользователя
        2. Ввод сгенерированных данных в соотвутствующие поля
        3. Проверка сообщения об ошибке
        4. Провека текущего адреса

        Ожидаемый результат - текущая url драйвера соответствует url страницы регистрации
        """
        page = self._registration(agree=False)
        assert page.url == self.driver.current_url

    @pytest.mark.positive
    def test_go_to_login(self):
        """
        Тест страницы регистрации - возврат на страницу входа
        1. Переход на страницу регистрации
        2. Переход на страницу входа
        3. Проверка url текущей страницы

        Ожидаемый результат - текущая url драйвера соответствует url страницы входа
        """
        registration_page = self.start_page.go_to_registration()
        login_page = registration_page.go_to_login()
        assert login_page.url == self.driver.current_url

@pytest.mark.UI
class TestMainPageAutoLogin(BaseUITest):
    
    @pytest.mark.positive
    @pytest.mark.parametrize(
        ('text_elem', 'url'),
        [
            ('What is an API?','https://en.wikipedia.org/wiki/API'),
            ('Future of internet','https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/'),
            ('Lets talk about SMTP?', 'https://ru.wikipedia.org/wiki/SMTP')
        ]
    )
    def test_overlay_button_link(self,text_elem,url):
        """
        Тест главной страницы - переход на нужные страницы с overlay  кнопок
        1. Авторизироваться на сайте и попасть на главную страницу
        2. Нажать на кнопки overlay
        3. Проверить успешность перехода на новую страницу

        Ожидаемый результат - открылось новое окно с соответствующим url
        """
        windows = self.start_page.click_overlay(text_elem)
        self.start_page.change_window(windows)
        assert self.driver.current_url.find(url) != -1

    @pytest.mark.Bug
    @pytest.mark.positive
    @pytest.mark.parametrize(
        ('text_elem','text_hide_button', 'url'),
        [
            ('Python history','Python','https://en.wikipedia.org/wiki/History_of_Python'),
            ('About Flask','Python','https://flask.palletsprojects.com/en/1.1.x/#'),
        ]
    )
    def test_navbar_droplist_python(self, text_elem, text_hide_button, url):
        """
        Тест главной страницы - переход на нужные страницы с выпадающего меню Python
        1. Авторизироваться на сайте и попасть на главную страницу
        2. Открыть выпадающее меню
        3. Нажать на соответствующий пункт меню
        3. Проверить успешность перехода на новую страницу

        Ожидаемый результат - открылось новое окно с соответствующим url
        """
        windows = self.start_page.click_navber(text_locator=text_elem, text_locator_hide=text_hide_button)
        self.start_page.change_window(windows)
        assert self.driver.current_url.find(url) != -1

    @pytest.mark.Bug
    @pytest.mark.positive
    def test_navbar_python(self):
        """
        Баг. Тест главной страницы - переход на страницу Python
        1. Авторизироваться на сайте и попасть на главную страницу
        2. Открыть выпадающее меню
        3. Нажать на соответствующий пункт меню
        3. Проверить успешность перехода на новую страницу

        Ожидаемый результат - открылось новое окно с соответствующим url
        """
        windows = self.start_page.click_navber(text_locator='Python')
        self.start_page.change_window(windows)
        assert self.driver.current_url.find('https://www.python.org/') != -1

    @pytest.mark.Bug
    @pytest.mark.positive
    def test_navbar_droplist_linux(self):
        """
        Баг. Тест главной страницы - переход на нужные страницы с выпадающего меню Linux
        1. Авторизироваться на сайте и попасть на главную страницу
        2. Открыть выпадающее меню
        3. Нажать на соответствующий пункт меню
        3. Проверить успешность перехода на новую страницу

        Ожидаемый результат - открылось новое окно с соответствующим url
        """
        windows = self.start_page.click_navber(text_locator='Download Centos7', text_locator_hide='Linux')
        self.start_page.change_window(windows)
        assert self.driver.current_url.find('https://www.centos.org/download/') != -1

    @pytest.mark.positive
    @pytest.mark.parametrize(
        ('text_elem','text_hide_buttron', 'url'),
        [
            ('News','Network','https://www.wireshark.org/news/'),
            ('Download','Network','https://www.wireshark.org/#download'),
            ('Examples ','Network','https://hackertarget.com/tcpdump-examples/'),
        ]
    )
    def test_navbar_droplist_network(self,text_elem, text_hide_buttron, url):
        """
        Тест главной страницы - переход на нужные страницы с выпадающего меню Network
        1. Авторизироваться на сайте и попасть на главную страницу
        2. Открыть выпадающее меню
        3. Нажать на соответствующий пункт меню
        3. Проверить успешность перехода на новую страницу

        Ожидаемый результат - открылось новое окно с соответствующим url
        """
        windows = self.start_page.click_navber(text_locator=text_elem, text_locator_hide=text_hide_buttron)
        self.start_page.change_window(windows)
        assert self.driver.current_url.find(url) != -1

    @pytest.mark.positive
    def test_logout(self):
        """
        Тест главной страницы - выход из системы 
        1. Авторизироваться на сайте и попасть на главную страницу
        3. Нажать на кнопку выхода
        3. Проверить успешность выхода из системы

        Ожидаемый результат - текущая url драйвера соответствует url страницы входа
        """
        login_page = self.start_page.logout()
        assert login_page.url == self.driver.current_url

    @pytest.mark.Bug
    @pytest.mark.positive
    def test_click_navbar_with_minimal_window(self):
        """
        Баг. Тест главной страницы - нажатие кнопки домой в умньшенном размере окна
        1. Авторизироваться на сайте и попасть на главную страницу
        3. Нажать кнопку домой
        3. Проверить успешность перехода на новую страницу

        Ожидаемый результат - страница перезагрузилась
        """
        self.start_page.driver.set_window_size(700, 900)
        self.start_page.click_navber(text_locator='HOME')
        assert self.start_page.url == self.driver.current_url

    @pytest.mark.negative
    def test_exist_vk_id(self):
        """
        Тест главной страницы - проверка наличия vk_id на странице 
        1. Авторизироваться на сайте и попасть на главную страницу
        2. Проверить наличие vk_id на странице

        Ожидаемый результат - элемент vk_id не будет найден
        """
        assert self.start_page.find_vk_id

@pytest.mark.UI
class TestMainPageManualLogin(BaseUITest):
    autologin = False

    @pytest.mark.positive
    def test_vk_id(self):
        """
        Тест главной страницы - проверка наличия vk_id на странице 
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Отправить в mock id пользователя
        3. Авторизироваться на сайте и попасть на главную страниц
        5. Проверить текст в vk_id

        Ожидаемый результат - полученыый vk_id совпадет с отправленным в mock
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        self.mock_client.request(method='POST',username=user.username, data='id_qa')
        main_page = self.start_page.login(username=user.username, password=user.password)
        assert main_page.find_vk_id == 'VK ID: id_qa'

    @pytest.mark.positive
    def test_vk_id_over_length(self):
        """
        Тест главной страницы - проверка доступа к кнопке выхода при большом id
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Отправить в mock id пользователя
        3. Авторизироваться на сайте и попасть на главную страниц
        5. Проверить текст в vk_id
        6. Попытаться выйти из системы

        Ожидаемый результат - полученыый vk_id совпадет с отправленным в mock
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        self.mock_client.request(method='POST',username=user.username, data='id_qa'*200)
        main_page = self.start_page.login(username=user.username, password=user.password)
        assert main_page.find_vk_id == f'VK ID: {"id_qa"*200}'
        login_page = main_page.logout()
        assert login_page.url == self.driver.current_url

    # Мб параметризацию с изменением имени
    @pytest.mark.positive
    def test_username_on_page(self):
        """
        Тест главной страницы -  проверка наличия имени пользователя на странице 
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Авторизироваться на сайте и попасть на главную страниц
        5. Проверить имя на странице

        Ожидаемый результат - полученное имя совпадет с даннымив БД
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        main_page = self.start_page.login(username=user.username, password=user.password)
        assert main_page.find_elem(main_page.locators.LOGIN_NAME) == f'Logged as {user.password}'
