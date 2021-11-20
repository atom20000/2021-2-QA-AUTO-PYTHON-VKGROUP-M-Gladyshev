from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
from models.models import *
import sqlalchemy

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
        self.session = sessionmaker(bind=self.connection.engine)()

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

    def create_table(self,name_table):
        if not inspect(self.engine).has_table(name_table):
            Base.metadata.tables[name_table].create(self.engine)

    def insert_rows(self,insert_values):
        for ins_va in insert_values:
            self.insert_row(ins_va)

    def insert_row(self,insert_value):
        self.session.add(insert_value)
        self.session.commit()

    def select_all_rows(self,entities):
        self.session.commit()
        return self.session.query(entities).all()