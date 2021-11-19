import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MySQLORMClient():

    def __init__(self,user,password,db_name,host='127.0.0.1',port=3306):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.port = port
    
    def connect(self, created_db=True):
        db = self.db_name if created_db else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url, encoding='utf-8')
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine)

    def recreate_db(self):
        self.connect(created_db=False)
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)
        self.connection.close()
        self.connect()
        

    def execute_query(self, query, fetch=True):
        result = self.connection.execute(query)
        if fetch:
            return result.fetchall()

    def insert_rows(self):
        pass

    def insert_row(self):
        pass