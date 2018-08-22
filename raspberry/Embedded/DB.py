import pymongo

class DB:
    def __init__(self, ip = 'localhost', port = 27017, table="employees"):
        self.client     = pymongo.MongoClient(ip, port)
        self.db         = self.client.SFSH
        self.collection = self.db[table]

        self.buffer = {
            '_id'       : None,
            'name'      : None,
            'sleep'     : None,
            'temper'    : None,
            'connected' : None,
            'WiFi'      : None
        }

        self.fieldList = ['_id', 'name', 'sleep', 'temper', 'connected', 'WiFi']

    def bufferInit(self):
        self.buffer = {
            '_id'       : None,
            'name'      : None,
            'sleep'     : None,
            'temper'    : None,
            'connected' : None,
            'WiFi'      : None
        }

    def isExist(self, id, name):
        return self.collection.find_one({"name" : name, "_id" : id}) is not None

    def getLastID(self):
        value = self.collection.find().sort("_id", pymongo.DESCENDING)[0]["_id"]
        if value : return value
        else     : return 0

    def getData(self, name, id=None):
        if id is None:
            return self.collection.find({"name" : name})
        else:
            return self.collection.find_one({"name" : name, "_id" : id})

    def setData(self, field, data):
        if field in self.fieldList:
            self.buffer[field] = data
        else:
            raise ValueError('buffer has no attribute {}'.format(field))

    def setBuffer(self, post):
        if post.keys() == self.buffer.keys():
            self.buffer = post
        else:
            raise ValueError("post keys and buffer keys don't match : {}, {}".format(post.keys(), self.buffer.keys()))

    def upload(self):
        for key in self.buffer.keys():
            if self.buffer[key] is None:
                raise ValueError('{} field value is None.'.format(key))

        key = {"_id" : self.buffer["_id"]}

        if self.collection.find_one(key) is None:
            self.collection.insert(self.buffer)
        else:
            self.collection.update(key, self.buffer)

        self.bufferInit()

    def __del__(self):
        self.client.close()

