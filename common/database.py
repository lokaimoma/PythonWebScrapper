import pymongo
import os

class Database:
    # original url for local "mongodb://127.0.0.1:27017/clarkdb"
    url = os.environ.get('MONGOLAB_URI')
    DATABASE = pymongo.MongoClient(url).get_database()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    