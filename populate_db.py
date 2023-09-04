from sqlmodel import Session, select
from main import engine
from models import AuctionItem
import random


def create_auct_item():
    r = random.randint(1,100)
    item_name = f'Painting number {r}'
    item_description = f'Description for painting number {r}'
    min_price = random.randint(5000,20000)
    price_step = min_price/10
    return AuctionItem(item_name=item_name, item_description=item_description,
                       min_price=min_price, price_step=price_step)


def create_auct_db():
    items = [create_auct_item() for _ in range(10)]
    with Session(engine) as session:
        session.add_all(items)
        session.commit()


def select_auction_item():
    with Session(engine) as session:  # 
        statement = select(AuctionItem)  # 
        results = session.exec(statement)  # 
        for auction_item in results:  # 
            print(auction_item) 
            
create_auct_db()
# select_auction_item()