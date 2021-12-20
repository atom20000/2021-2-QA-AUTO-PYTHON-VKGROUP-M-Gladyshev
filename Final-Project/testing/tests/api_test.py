from tests.base import BaseAPITest
import pytest
import allure

@pytest.mark.API
class TestLoginAPI(BaseAPITest):

    autologin = False

    @pytest.mark.positive
    def test_login_positive(self):
        """
        Тест входа через API - успешный вход
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Авторизация пользователя 
        4. Проверка статуса ответа

        Ожидаемый результат - статус код ответа 302
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        response = self.api_client.login(username=user.username, password=user.password)
        with allure.step('Check that the status code and active'):
            assert response.status_code == 302
            assert self.mysql_client.select_user(username=user.username).active == 1

    @pytest.mark.negative
    def test_login_negative_non_existent_user(self):
        """
        Негативный тест входа через API - вход под несуществующем пользователем
        1. Генерируется валидный объект данных пользователя
        3. Попытка вторизации пользователя 
        4. Проверка статуса ответа

        Ожидаемый результат - статус код ответа 401
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        response = self.api_client.login(username=user.username, password=user.password)
        with allure.step('Check that the status code'):
            assert response.status_code == 401

    @pytest.mark.negative
    def test_login_negative_invalid_username(self):
        """
        Негативный тест входа через API - вход в существующего пользователя с вводом пустого `username`
        1. Генерируется валидный объект данных пользователя
        3. Попытка вторизации пользователя 
        4. Проверка статуса ответа
        5. Проверка поля `active` в БД

        Ожидаемый результат - статус код ответа 200, статус `active` None
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        response = self.api_client.login(username='', password=user.password)
        with allure.step('Check that the status code and active'):
            assert response.status_code == 200
            assert self.mysql_client.select_user(username=user.username).active == None

    @pytest.mark.negative
    def test_login_negative_invalid_username(self):
        """
        Негативный тест входа через API - вход в существующего пользователя с вводом пустого `password`
        1. Генерируется валидный объект данных пользователя
        3. Попытка вторизации пользователя 
        4. Проверка статуса ответа
        5. Проверка поля `active` в БД

        Ожидаемый результат - статус код ответа 200, статус `active` None
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        response = self.api_client.login(username=user.username, password='')
        with allure.step('Check that the status code and active'):
            assert response.status_code == 200
            assert self.mysql_client.select_user(username=user.username).active == None

@pytest.mark.API
class TestRegistrationAPI(BaseAPITest):

    autologin = False

    @pytest.mark.positive
    def test_registration(self):
        """
        Тест регистрации чеерез API - пользователь успешно зарегеистрировался и вошел в систему
        1. Генерируется валидный объект данных пользователя
        2. Регистрация пользователя 
        3. Проверка статуса ответа
        4. Проверить зарегистрированного пользователя в БД

        Ожидаемый результат - статус код ответа 302, статус `active` 1
        """
        result = self._registration()
        with allure.step('Check that the status code and active'):
            assert result['response'].status_code == 302
            assert self.mysql_client.select_user(username=result['user'].username).active == 1

    @pytest.mark.Bug
    @pytest.mark.negative
    def test_negative_registration_russian_text(self):
        """
        Баг. Негативный тест регистрации через API - имя пользователя на русском языке
        1. С параметром `багбаг` генерируется объект данных пользователя
        2. Регистрация пользователя 
        3. Провека статуса ответа

        Ожидаемый результат - статус код ответа 302
        """
        response = self._registration(username='багбаг')['response']
        with allure.step('Check that the status code'):
            assert response.status_code == 302

    @pytest.mark.negative
    @pytest.mark.parametrize(
        ('username'),
        [
            ('qa'),
            ('qa'*9)
        ]
    )
    def test_negative_registration_invalid_username(self,username):
        """
        Параметризированный негативный тест регистрации через API - имя пользователя невалидной длины
        1. С параметром `username` генерируется объект данных пользователя
        2. Регистрация пользователя 
        3. Провека статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код 400, в БД нет записи с данным пользователем
        """
        response = self._registration(username=username)['response']
        with allure.step('Check that the status code and DB'):
            assert response.status_code == 400
            assert len(self.mysql_client.select_user(username=username)) == 0
    

    @pytest.mark.negative
    def test_negative_registration_invalid_password(self):
        """
        Параметризированный негативный тест регистрации через API - пароль пользователя невалидной длины
        1. С параметром `password` генерируется объект данных пользователя
        2. Регистрация пользователя 
        3. Провека статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код 400, в БД нет записи с данным пользователем
        """
        result = self._registration(password='qa'*128)
        with allure.step('Check that the status code and DB'):
            assert result['response'].status_code == 400
            assert len(self.mysql_client.select_user(username=result['user'].username)) == 0

    @pytest.mark.negative
    @pytest.mark.parametrize(
        ('email'),
        [
            ('qa'),
            ('qa'*33),
            ('@studx.ru'),
            ('soon@studx,ru.ru')
        ]
    )
    def test_negative_registration_invalid_email(self,email):
        """
        Параметризированный негативный тест регистрации через API - почта пользователя невалидна
        1. С параметром `email` генерируется объект данных пользователя
        2. Регистрация пользователя 
        3. Провека статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код 400, в БД нет записи с данным пользователем
        """
        result = self._registration(email=email)
        with allure.step('Check that the status code and DB'):
            assert result['response'].status_code == 400
            assert len(self.mysql_client.select_user(username=result['user'].username)) == 0

    @pytest.mark.negative
    def test_negative_registration_invalid_repassword(self):
        """
        Негативный тест регистрации через API - повтор пароля пользователя невалидный
        1. С параметрами `passwor` и `repassword` генерируется объект данных пользователя
        2. Регистрация пользователя 
        3. Провека статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код 400, в БД нет записи с данным пользователем
        """
        result = self._registration(repassword='1234',password='12')
        with allure.step('Check that the status code and DB'):
            assert result['response'].status_code == 400
            assert len(self.mysql_client.select_user(username=result['user'].username)) == 0


    @pytest.mark.negative
    def test_negative_registration_with_exist_email(self):
        """
        Негативный тест регистрации через API - создание пользователя с уже зарегистрированной почтой
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. С параметром `email` генерируется объект данных пользователя
        4. Регистрация пользователя 
        3. Провека статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код 500, в БД одна запись с данным пользователем
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        result = self._registration(email=user.email)
        with allure.step('Check that the status code and DB'):
            assert result['response'].status_code == 500
            assert len(self.mysql_client.select_user(username=result['user'].username)) == 1

    @pytest.mark.negative
    def test_negative_reregistration_exist_user(self):
        """
        Негативный тест регистрации через API - повторная регистрация существующего пользователя 
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Регистрация пользователя 
        3. Провека статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код 409, в БД одна запись с данным пользователем
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        response = self.api_client.registration(
            username=user.username, 
            email=user.email, 
            password=user.password, 
            repassword=user.password)
        with allure.step('Check that the status code and DB'):
            assert response.status_code == 409
            assert len(self.mysql_client.select_user(username=user.username)) == 1

    @pytest.mark.negative
    def test_negative_registration_dont_accept(self):
        """
        Негативный тест регистрации через API - не приняты условия соглашения  пользователя 
        1. Генерируется валидный объект данных пользователя
        2. Регистрация пользователя 
        3. Провека статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код 400, в БД нет записи с данным пользователем
        """
        result = self._registration(term='n')
        with allure.step('Check that the status code and DB'):
            assert result['response'].status_code == 400
            assert len(self.mysql_client.select_user(username=result['user'].username)) == 0

@pytest.mark.API
class TestAPI(BaseAPITest):

    @pytest.mark.positive
    def test_add_user(self):
        """
        Тест добавление пользователя через API - успешное добавление 
        1. Генерируется валидный объект данных пользователя
        2. Отправить с помощью API данные пользователя для создания
        3. Проверка статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код ответа 201, в БД одна запись с данным пользователем
        """
        user = self.mysql_client.generate_user()
        response = self.api_client.add_user(username=user.username, 
            email=user.email, 
            password=user.password)
        with allure.step('Check that the status code and DB'):
            assert response.status_code == 201
            assert len(self.mysql_client.select_user(username=user.username)) == 1

    @pytest.mark.negative
    def test_negative_add_user(self):
        """
        Негативный тест добавление пользователя через API - добавление существующего пользователя
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Отправить с помощью API данные пользователя для создания
        4. Проверка статуса ответа
        5. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код ответа 304, в БД одна запись с данным пользователем
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        response = self.api_client.add_user(username=user.username, 
            email=user.email, 
            password=user.password)
        with allure.step('Check that the status code and DB'):
            assert response.status_code == 304
            assert len(self.mysql_client.select_user(username=user.username)) == 1

    @pytest.mark.positive
    def test_delete_user(self):
        """
        Тест удаления пользователя через API - удаление существующего пользователя
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Удалть с помощью API данные пользователя 
        4. Проверка статуса ответа
        5. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код ответа 204, в БД нет запись с данным пользователем
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        response = self.mysql_client.get_request(
            url=f'api/del_user/{user.username}',
            headers=None,
            data=None
        )
        with allure.step('Check that the status code and DB'):
            assert response.status_code == 204
            assert len(self.mysql_client.select_user(username=user.username)) == 0

    @pytest.mark.negative
    def test_delete_non_exist_user(self):
        """
        Негативный тест удаления пользователя через API - удаление не существующего пользователя
        1. Генерируется валидный объект данных пользователя
        2. Удалть с помощью API данные пользователя 
        3. Проверка статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код ответа 404, в БД нет запись с данным пользователем
        """
        user = self.mysql_client.generate_user()
        response = self.mysql_client.get_request(
            url=f'api/del_user/{user.username}',
            headers=None,
            data=None
        )
        with allure.step('Check that the status code and DB'):
            assert response.status_code == 404
            assert len(self.mysql_client.select_user(username=user.username)) == 0

    @pytest.mark.positive
    def test_block_user(self):
        """
        Тест блокировки пользователя через API - блокировка существующего пользователя
        1. Генерируется валидный объект данных пользователя
        2. Отправка данных в БД
        3. Блокировка с помощью API данного пользователя 
        4. Проверка статуса ответа
        5. Проверка статуса пользователя в БД

        Ожидаемый результат - статус код ответа 200, в БД статус доступа пользователя 0
        """
        user = self.mysql_client.generate_user()
        self.mysql_client.insert_row(user)
        response = self.mysql_client.get_request(
            url=f'api/block_user/{user.username}',
            headers=None,
            data=None
        )
        with allure.step('Check that the status code and access'):
            assert response.status_code == 200
            assert self.mysql_client.select_user(username=user.username).access == 0

    @pytest.mark.negative
    def test_block_non_exist_user(self):
        """
        Негативный тест блокировки пользователя через API - блокировка не существующего пользователя
        1. Генерируется валидный объект данных пользователя
        2. Блокировка с помощью API данного пользователя 
        3. Проверка статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код ответа 404, в БД нет запись с данным пользователем
        """
        user = self.mysql_client.generate_user()
        response = self.mysql_client.get_request(
            url=f'api/block_user/{user.username}',
            headers=None,
            data=None
        )
        with allure.step('Check that the status code and DB'):
            assert response.status_code == 404
            assert len(self.mysql_client.select_user(username=user.username)) == 0

    @pytest.mark.negative
    def test_block_blocked_user(self):
        """
        Негативный тест блокировки пользователя через API - блокировка заблокированного пользователя
        1. Генерируется валидный объект данных пользователя c `access` 0
        2. Отправка данных в БД
        3. Блокировка с помощью API данного пользователя 
        4. Проверка статуса ответа
        5. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код ответа 304, в БД статус доступа пользователя 0
        """
        user = self.mysql_client.generate_user(access=0)
        self.mysql_client.insert_row(user)
        response = self.mysql_client.get_request(
            url=f'api/block_user/{user.username}',
            headers=None,
            data=None
        )
        with allure.step('Check that the status code and access'):
            assert response.status_code == 304
            assert self.mysql_client.select_user(username=user.username).access == 0

    @pytest.mark.positive
    def test_accept_user(self):
        """
        Тест разблокировки пользователя через API - блокировка существующего пользователя
        1. Генерируется валидный объект данных пользователя c `access` 0
        2. Отправка данных в БД
        3. Разблокировка с помощью API данного пользователя 
        4. Проверка статуса ответа
        5. Проверка статуса пользователя в БД

        Ожидаемый результат - статус код ответа 200, в БД статус доступа пользователя 1
        """
        user = self.mysql_client.generate_user(access=0)
        self.mysql_client.insert_row(user)
        response = self.mysql_client.get_request(
            url=f'api/accept_user/{user.username}',
            headers=None,
            data=None
        )
        with allure.step('Check that the status code and access'):
            assert response.status_code == 200
            assert self.mysql_client.select_user(username=user.username).access == 1

    @pytest.mark.negative
    def test_accept_non_exist_user(self):
        """
        Негативный тест разблокировки пользователя через API - разблокировка не существующего пользователя
        1. Генерируется валидный объект данных пользователяc `access` 0
        2. Разблокировка с помощью API данного пользователя 
        3. Проверка статуса ответа
        4. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код ответа 404, в БД нет запись с данным пользователем
        """
        user = self.mysql_client.generate_user(access=0)
        response = self.mysql_client.get_request(
            url=f'api/accept_user/{user.username}',
            headers=None,
            data=None
        )
        assert response.status_code == 404
        assert len(self.mysql_client.select_user(username=user.username)) == 0

    @pytest.mark.negative
    def test_accept_accpted_user(self):
        """
        Негативный тест разблокировки пользователя через API - разблокировка заблокированного пользователя
        1. Генерируется валидный объект данных пользователя c `access` 0
        2. Отправка данных в БД
        3. Разблокировка с помощью API данного пользователя 
        4. Проверка статуса ответа
        5. Проверка наличия пользователя в БД

        Ожидаемый результат - статус код ответа 304, в БД статус доступа пользователя 1
        """
        user = self.mysql_client.generate_user(access=0)
        self.mysql_client.insert_row(user)
        response = self.mysql_client.get_request(
            url=f'api/accept_user/{user.username}',
            headers=None,
            data=None
        )
        with allure.step('Check that the status code and DB'):
            assert response.status_code == 304
            assert self.mysql_client.select_user(username=user.username).access == 1

    @pytest.mark.positive
    def test_logout(self):
        """
        Тест выхода пользователя через API - блокировка существующего пользователя
        1. Генерируется валидный объект данных пользователя c `access` 1
        2. Отправка данных в БД
        3. Выход с помощью API данного пользователя 
        4. Проверка статуса ответа
        5. Проверка статуса пользователя в БД
        """

    @pytest.mark.positive
    def test_find_me_js_api(self):
        """
        Тестстатического файла  find_me - файл возвращается по запросу
        1. Отправить запрос 
        2. Проверить ответ
        Ожидаемый результат: статус код 200
        """
        response = self.mysql_client.get_request(
            url=f'/static/scripts/findMeError.js',
            headers=None,
            data=None
        )
        with allure.step('Check that the status code'):
            assert response.status_code == 200