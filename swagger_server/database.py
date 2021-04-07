import os
import pymongo

mongo = pymongo.MongoClient(os.getenv("DATABASE_URL"))
