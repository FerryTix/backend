import os
import pymongo
from bson import ObjectId, UuidRepresentation

mongo = pymongo.MongoClient(
    os.getenv("DATABASE_URL"),
    uuidRepresentation='standard'
)


def convert_mongo_id_to_id(data: dict) -> dict:
    """
    Converts a dict-entry with key '_id' (used in Mongo schema) to key 'id' (used in GraphQL schema).
    :param data: dict to convert
    :return: dict
    """
    if "_id" in data.keys():
        object_id = data["_id"]
        data["uuid"] = str(object_id)
        del data["_id"]
    return data


def convert_id_to_mongo_id(data: dict) -> dict:
    """
    Converts a dict-entry with key 'id' (used in GraphQL schema) to key '_id' (used in Mongo schema).
    :param data: dict to convert
    :return: dict
    """
    if "id" in data.keys():
        object_id = data["uuid"]
        data["_id"] = ObjectId(object_id)
        del data["uuid"]
    return data


def remove_mongo_object_id(data: dict) -> dict:
    """
    removes any object id created by mongodb
    :param data:
    :return:
    """
    if "_id" in data.keys():
        del data["_id"]
    return data
