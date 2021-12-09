# Легкие настройки
Путь до access.log лежит в ```static_var.py``` в переменной ```PATH_ACCESS_LOG_FILE```.  
Тесты можно запуска с помощью марка ```-m SQL```.  
Теперь переменные ```USER_NAME, USER_PASSWORD, DB_NAME, HOST, PORT```
задаются через переменные окружения.  
Пример запуска тестов ```USER_NAME=root USER_PASSWORD=pass DB_NAME=TEST_SQL HOST=172.30.32.1 PORT=3306 pytest -m SQL```.  