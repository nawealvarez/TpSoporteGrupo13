from pymongo import MongoClient

class Connection():
    def connect(self):
        client = MongoClient(host=['localhost:27017'])
        return client.test