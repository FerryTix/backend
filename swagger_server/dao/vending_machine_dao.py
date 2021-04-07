from typing import Optional, List

from pymongo.collection import Collection

from swagger_server.models import VendingMachine
from swagger_server import database as db

from uuid import uuid4

vending_machine_db: Collection = db.mongo.faehrtrade.vendingmachine


def get_all_machines() -> Optional[List[VendingMachine]]:
    result = vending_machine_db.find({})
    machine_list = [VendingMachine(**db.remove_mongo_object_id(r)) for r in result]
    get_uuid()
    return machine_list


def get_uuid():
    print(uuid4())
