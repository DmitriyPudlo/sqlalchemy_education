from sqlalchemy import create_engine, Column, Integer, String, Interval, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    books = relationship("Book")


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    id_publisher = Column(Integer, ForeignKey('publisher.id'))
    publisher = relationship("Publisher")
    stock = relationship('Stock')


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    stock = relationship('Stock')


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    count = Column(Integer, nullable=False)
    id_book = Column(Integer, ForeignKey('book.id'))
    books = relationship('Book')
    id_shop = Column(Integer, ForeignKey('shop.id'))
    shop = relationship('Shop')
    sale = relationship('Sale')


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    date_sale = Column(Interval, nullable=False)
    id_stock = Column(Integer, ForeignKey('stock.id'))
    stock = relationship('Stock')


if __name__ == '__main__':
    metadata = MetaData()
    engine = create_engine("postgresql+psycopg2://postgres:3616@localhost/postgres", echo=True)
    engine.connect()
    Base.metadata.create_all(engine)
