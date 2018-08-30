import pymongo

class DB:
    def __init__(self, ip = 'localhost', port = 27017, table="admin"):
        self.client     = pymongo.MongoClient(ip, port)
        self.db         = self.client.SFSH
        self.collection = self.db[table]

    def changeCollection(self, table):
        if type(table) == str:
            self.collection = self.db[table]

    def __del__(self):
        self.client.close()

