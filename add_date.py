from models import Publisher, Book, Shop, Stock, Sale
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json


engine = create_engine("postgresql+psycopg2://postgres:3616@localhost/postgres", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r') as dates_json:
    dates = json.load(dates_json)


model = {'publisher': Publisher, 'shop': Shop, 'book': Book, 'stock': Stock, 'sale': Sale}
for row in dates:
    name_model = model[row['model']]
    session.add(name_model(id=row['pk'], **row['fields']))
    session.commit()
