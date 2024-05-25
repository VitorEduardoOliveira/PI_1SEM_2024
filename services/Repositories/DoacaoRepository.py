from core.services.MongoService import MongoService

class MongoRepository:
    def __init__(self, mongo_service: MongoService):
        self.db = mongo_service.db
        self.collection = self.db["doacoes"]

    def get_alimento_mais_doado(self, id_campanha=None):
        match_filtro = {
            "$match": {
                "alimento": {"$ne": None}
            }
        }

        if id_campanha is not None:
            match_filtro["$match"]["id_campanha"] = id_campanha

        pipeline = [
            match_filtro,
            {
                "$group": {
                    "_id": "$alimento",
                    "totalQuantity": {"$sum": "$qtde"}
                }
            },
            {
                "$sort": {"totalQuantity": -1}
            },
            {
                "$limit": 1
            }
        ]
        result = list(self.collection.aggregate(pipeline))
        return result
    
    def get_total_alimentos(self, alimento):
        pipeline = [
            {
                "$match": {
                    "alimento": {"$ne": None}
                }
            },
            {
                "$match": {
                    "alimento": alimento
                }
            },
            {
                "$group": {
                    "_id": "$alimento",
                    "totalQuantidade": {"$sum": "$qtde"}
                }
            }
        ]
        result = list(self.collection.aggregate(pipeline))
        if result:
            return result[0]["totalQuantidade"]
        return 0
    
    def get_alimentos_doados_por_campanha(self, id_campanha):
        pipeline = [
            {
                "$match": {
                    "id_campanha": id_campanha,
                    "alimento": {"$ne": None}
                }
            },
            {
                "$group": {
                    "_id": "$alimento",
                    "totalQuantidade": {"$sum": "$qtde"}
                }
            }
        ]
        result = list(self.collection.aggregate(pipeline))
        return result
    
    def get_doacoes_alimento_por_campanha(self, id_campanha):
        pipeline = [
            {
                "$match": {
                    "id_campanha": id_campanha,
                    "alimento": {"$ne": None}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "data": 1,
                    "alimento": 1,
                    "qtde": 1,
                    "doador": 1
                }
            }
        ]
        result = list(self.collection.aggregate(pipeline))
        return result
    
    def get_doacoes_dinheiro_por_campanha(self, id_campanha):
        pipeline = [
            {
                "$match": {
                    "id_campanha": id_campanha,
                    "dinheiro": {"$ne": None}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "dinheiro": 1,
                    "doador": 1
                }
            }
        ]
        result = list(self.collection.aggregate(pipeline))
        return result
    
    def insert_one(self, document):
        result = self.collection.insert_one(document)
        return result.inserted_id

    def find_one(self, query):
        document = self.collection.find_one(query)
        return document

    def find_many(self, query):
        documents = self.collection.find(query)
        return list(documents)

    def update_one(self, query, update_values):
        result = self.collection.update_one(query, {"$set": update_values})
        return result.modified_count

    def delete_one(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count

    def delete_many(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count