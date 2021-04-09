from typing import Optional, List

from pymongo.collection import Collection

from swagger_server.models import FaehrCard
from swagger_server import database as db

faehrcard_db: Collection = db.mongo.ferrytix.faehrcard


def find_by_uuid(uuid: str) -> Optional[FaehrCard]:
    result = faehrcard_db.find_one({"uuid": uuid})

    if result:
        return FaehrCard(**db.remove_mongo_object_id(result))
    else:
        return None


def find_balance_by_uuid(uuid: str) -> Optional[FaehrCard]:
    result = faehrcard_db.find_one({"uuid": uuid})

    if result:
        del result["uuid"]
        del result["owned_by"]
        del result["issued_by"]
        del result["issued_at"]
        del result["_id"]

        return result
    else:
        return None
