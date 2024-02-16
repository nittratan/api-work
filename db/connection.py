from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.users = None

    def connect_to_mongodb(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["fastapi_db"]
        self.users = self.db["users"]

    def close_mongodb_connection(self):
        self.client.close()

db = Database()
