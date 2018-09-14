from pymongo import MongoClient

class Connection(object):
    def connect(self):
        client = MongoClient(host=['localhost:27017'])
        return client.AverSiAhorra
