from flask import json
from pymongo.results import UpdateResult
from typing import Optional, List

from pymongo.collection import Collection

from swagger_server import database as db
from swagger_server.models import Payment

payment_db: Collection = db.mongo.ferrytix.payment


def insert(payment: Payment) -> Optional[str]:
    new_payment = payment.to_dict()
    result = payment_db.insert_one(new_payment)
    if result.inserted_id != "":
        return str(result.inserted_id)
    else:
        return None


def find_by_id(uuid: str) -> Optional[Payment]:
    result = payment_db.find_one({"uuid": uuid})
    if result:
        return Payment(**db.remove_mongo_object_id(result))
    else:
        return None


def update(payment: Payment) -> Optional[bool]:
    result: UpdateResult = payment_db.update_one({"uuid": payment.uuid}, {"$set": payment})
    return result.matched_count == 1
