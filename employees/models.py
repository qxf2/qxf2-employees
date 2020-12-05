"""
Models for the employee app
"""
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/employee_database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,\
    bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Employee(Base):
    __tablename__ = 'employee'
    email = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    employee_id = Column(String)
    skype_id = Column(String)
    blog_author_name = Column(String)
    phone = Column(String)
    github_id = Column(String)
    aws_id = Column(String)
    trello_id = Column(String)
    date_joined = Column(String)
    employment_type = Column(String)
    is_active = Column(String)