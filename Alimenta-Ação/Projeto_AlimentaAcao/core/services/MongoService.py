from core.services.ConnectionService import ConnectionService

class MongoService:
  def __init__(self, connection: ConnectionService, dbname):
    self.client = connection.getConnection()
    self.db = self.client[dbname]