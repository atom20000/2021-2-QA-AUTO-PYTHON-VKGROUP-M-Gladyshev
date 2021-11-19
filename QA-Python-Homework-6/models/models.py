from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TemplateTwoColumnTable(Base):

    __tableargs__ = {'mysql_charset':'utf8'}

    def __init__(self,column_one,column_two,table_name, **kwargs):
        setattr(self,' __tablename__',table_name)
        setattr(self,column_one,Column(String))
        setattr(self,column_two,Column(Integer))
        super().__init__(**kwargs)

