from typing import Optional, List

from pymongo.collection import Collection

from swagger_server import database as db
from swagger_server.models import TicketSaleFaehrCard, TicketSaleCash

ticket_sale_db: Collection = db.mongo.ferrytix.ticket_sale


def insert_faehrcard(ticket_sale_faehrcard: TicketSaleFaehrCard) -> Optional[str]:
    new_ticket_sale = ticket_sale_faehrcard.to_dict()
    result = ticket_sale_db.insert_one(new_ticket_sale)
    if result.inserted_id != "":
        return str(result.inserted_id)
    else:
        return None


def insert_cash(ticket_sale_cash: TicketSaleCash) -> Optional[str]:
    result = ticket_sale_db.insert_one(ticket_sale_cash)
    if result.inserted_id != "":
        return str(result.inserted_id)
    else:
        return None