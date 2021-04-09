from typing import Optional, List

from pymongo.collection import Collection

from swagger_server.models import VendingMachine
from swagger_server import database as db

from uuid import uuid4

vending_machine_db: Collection = db.mongo.ferrytix.vendingmachine


def get_all_machines() -> Optional[List[VendingMachine]]:
    result = vending_machine_db.find({})
    machine_list = [VendingMachine(**db.remove_mongo_object_id(r)) for r in result]
    get_uuid()
    return machine_list


def find_machine_my_uuid(uuid: str) -> Optional[VendingMachine]:
    result = vending_machine_db.find({uuid: uuid})
    if result:
        return VendingMachine(**db.remove_mongo_object_id(result))
    else:
        return None


def get_uuid():
    print(uuid4())
