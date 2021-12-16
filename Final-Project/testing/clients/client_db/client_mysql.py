from sqlalchemy.orm import sessionmaker
from models import TestUsers
import sqlalchemy
from faker import Faker

faker : Faker = Faker()

class MySQLORMClient():

    def __init__(self,user,password,db_name='QA_myapp',host='mysql',port=3306):
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

    def insert_rows(self,insert_values):
        for ins_va in insert_values:
            self.insert_row(ins_va)

    def insert_row(self,insert_value):
        self.session.add(insert_value)
        self.session.commit()
    
    def delete_row(self, delete_user):
        self.session.commit()
        self.session.query(TestUsers).filter(TestUsers.username == delete_user).delete()
        self.session.commit()

    def select_user(self,username):
        self.session.commit()
        return self.session.query(TestUsers).filter(TestUsers.username == username).all()

    def generate_user(self, username=None, password=None, email=None, access=None, active=None, start_active_time=None):
        if username is None:
            username = faker.bothify('??????')
        if password is None:
            password = faker.password()
        if email is None:
            email = faker.email()
        if access is None:
            access = 1
        
        return TestUsers(
            username=username, 
            password=password,
            email=email,
            access=access,
            active=active,
            start_active_time=start_active_time
            )