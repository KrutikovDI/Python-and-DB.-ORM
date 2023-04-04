import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json

from models import create_tables, Publisher, Shop, Book, Stock, Sale

login = 'postgres'
password = 'Danil367173'
DSN = f'postgresql://{login}:{password}@localhost:5432/Python_ORM'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open ("Python и БД. ORM/tests_data.json") as f:
    test_dada = json.load(f)
for record in test_dada:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]

n = input('Введите имя издателя: ')
for c in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Sale.stock).join(Stock.shop).join(Stock.book).join(Book.publisher).filter(Publisher.name == n).all():
    print(*c, sep=" | ")

session.close()