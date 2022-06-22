import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):

    __tablename__ ="products"

    id =Column(Integer, primary_key=True)
    name = Column(String,)
    price = Column(Float, default=100.00)
    brand = Column(String)

class Users(Base):

    __tablename__ = "users"
    id =Column(Integer, primary_key=True)
    name = Column(String)
    college = Column(String)

if __name__ == "__main__":
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)


