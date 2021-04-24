from typing import Optional, List

from pymongo.collection import Collection

from swagger_server import database as db
from swagger_server.models import TopUp

top_up_db: Collection = db.mongo.ferrytix.top_up


# TODO: Functions have to be extended to support multiple top up solutions
def insert_cash(top_up: TopUp) -> Optional[str]:
    new_top_up = top_up.to_dict()
    result = top_up_db.insert_one(new_top_up)
    if result.inserted_id != "":
        return str(result.inserted_id)
    else:
        return None
