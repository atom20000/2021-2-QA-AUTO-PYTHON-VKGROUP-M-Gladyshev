from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta


Base = declarative_base(metaclass=DeclarativeMeta)

class CountAllRequest(Base):
    __tablename__ = 'CountAllRequest'
    __tableargs__ = {'mysql_charset':'utf8'}
    Count_All_Request = Column(Integer, primary_key=True)

    def __eq__(self,other):
        if not isinstance(other,CountAllRequest):
            return False
        return self.Count_All_Request == other.Count_All_Request

    def __repr__(self):
        return f'<{self.__tablename__}>\nCount_All_Request\n{self.Count_All_Request}\n'

class CountRequestByType(Base):
    __tablename__ = 'CountRequestByType'
    __tableargs__ = {'mysql_charset':'utf8'}
    Type = Column(String(500), primary_key=True)
    Count = Column(Integer)

    def __eq__(self,other):
        if not isinstance(other,CountRequestByType):
            return False
        return all([getattr(self,i) == getattr(other,i) for i in ['Type','Count']])

    def __repr__(self):
        return f'<{self.__tablename__}>\nCountRequestByType\n{self.Type}-{self.Count}\n'

class CountRequestByUrl(Base):
    __tablename__ = 'CountRequestByUrl'
    __tableargs__ = {'mysql_charset':'utf8'}
    Url = Column(String(500), primary_key=True)
    Count = Column(Integer)

    def __eq__(self,other):
        if not isinstance(other,CountRequestByUrl):
            return False
        return all([getattr(self,i) == getattr(other,i) for i in ['Url','Count']])

    def __repr__(self):
        return f'<{self.__tablename__}>\nCountRequestByUrl\n{self.Url}\n{self.Count}\n{"-"*10}\n'

class RequestBySizeWithError400(Base):
    __tablename__ = 'RequestBySizeWithError400'
    __tableargs__ = {'mysql_charset':'utf8'}
    Url = Column(String(500), primary_key=True)
    Status_code = Column(Integer)
    Size_request = Column(Integer)
    Ip = Column(String(500))

    def __eq__(self,other):
        if not isinstance(other,RequestBySizeWithError400):
            return False
        return all([getattr(self,i) == getattr(other,i) for i in ['Url','Status_code','Size_request','Ip']])

    def __repr__(self):
        return f'<{self.__tablename__}>\nRequestBySizeWithError400\n{self.Url}\n{self.Status_code}\n{self.Size_request}\n{self.Ip}\n{"-"*10}\n'

class CountRequestByIpWithError500(Base):
    __tablename__ = 'CountRequestByIpWithError500'
    __tableargs__ = {'mysql_charset':'utf8'}
    Ip = Column(String(500), primary_key=True)
    Count = Column(Integer)

    def __eq__(self,other):
        if not isinstance(other,CountRequestByIpWithError500):
            return False
        return all([getattr(self,i) == getattr(other,i) for i in ['Ip','Count']])

    def __repr__(self):
        return f'<{self.__tablename__}>\nCountRequestByIpWithError500\n{self.Ip}\n{self.Count}\n{"-"*10}\n'



#class TwoColumnTableMetaclass(DeclarativeMeta):
#    __abstract__ = True
#    __tableargs__ = {'mysql_charset':'utf8'}
# # column_one,column_two,table_name
#    def __new__(cls, name, bases, **kwargs):
#        dct = dict([('__tablename__',kwargs['table_name']),(kwargs['column_one'], Column(String, primary_key=True)), (kwargs['column_two'], Column(Integer))])
#        return super(TwoColumnTableMetaclass,cls).__new__(cls, name, bases, **dct)
#
#
#class test(Base, metaclass=TwoColumnTableMetaclass, fhjs='sfd'):
#    #meta_attrs = {'table_name':'test','column_one':'hfhf','column_two':'fdifdg'}
#    #__tablename__ = 'test'
#    #Base,metaclass=TwoColumnTableMetaclass('test',(Base,), {'table_name':'test','column_one':'hfhf','column_two':'fdifdg'})
#    #__metaclass__ = TwoColumnTableMetaclass('test',(object,), {'table_name':'test','column_one':'hfhf','column_two':'fdifdg'})
#    #column_one = Column(String, primary_key=True)
#    pass