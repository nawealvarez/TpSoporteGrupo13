from pymongo import MongoClient

class Connection:
    @staticmethod   
    def openConection(self):
        client = MongoClient(host=["localhost:27017"])
        return client.AverSiAhorra
