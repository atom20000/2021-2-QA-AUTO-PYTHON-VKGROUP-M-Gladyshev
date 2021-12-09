import os


PATH_ACCESS_LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),'.','log','access.log'))
USER_NAME = os.environ.get('USER_NAME') if os.environ.get('USER_NAME') else 'root'
USER_PASSWORD = os.environ.get('USER_PASSWORD') if os.environ.get('USER_PASSWORD') else 'pass'
DB_NAME = os.environ.get('DB_NAME') if os.environ.get('DB_NAME') else 'TEST_SQL'
HOST = os.environ.get('HOST') if os.environ.get('HOST') else '127.0.0.1'
PORT = os.environ.get('PORT') if os.environ.get('PORT') else '3306'