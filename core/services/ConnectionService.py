import pymongo

class ConnectionService:
  def getConnection(self):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client