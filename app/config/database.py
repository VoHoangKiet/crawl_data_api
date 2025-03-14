from pymongo import MongoClient
import os

class Database:
    def __init__(self):
        self.uri = os.getenv("MONGO_URI")
        self.client = MongoClient(self.uri)
        self.db = self.client['exe']
    
    def get_collection(self, collection_name):
        return self.db[collection_name]

db = Database()