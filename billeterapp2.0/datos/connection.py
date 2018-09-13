from pymongo import MongoClient

class Conn(object):
    def openConection(self):
        client = MongoClient(host=["localhost:27017"])
        #return client.AverSiAhorra
        return client.test

