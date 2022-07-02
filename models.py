from sqlalchemy import create_engine, Column, Integer, String, Interval, MetaData, ForeignKey, REAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = MetaData()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    id_publisher = Column(Integer, ForeignKey('publisher.id'))


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    count = Column(Integer, nullable=False)
    id_book = Column(Integer, ForeignKey('book.id'))
    id_shop = Column(Integer, ForeignKey('shop.id'))


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(REAL, nullable=False)
    count = Column(Integer, nullable=False)
    date_sale = Column(String(100), nullable=False)
    id_stock = Column(Integer, ForeignKey('stock.id'))


def creat_tables():
    engine = create_engine("postgresql+psycopg2://postgres:3616@localhost/postgres", echo=True)
    engine.connect()
    Base.metadata.create_all(engine)


creat_tables()
