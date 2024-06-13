from core.services.MongoService import MongoService

class CampanhaRepository:
    def __init__(self, mongo_service: MongoService):
        self.db = mongo_service.db
        self.collection = self.db["campanhas"]

    def get_detalhes_campanha(self, campaign_id):
        pipeline = [
            {
                "$match": {
                    "id": campaign_id
                }
            },
            {
                "$lookup": {
                    "from": "ongs",
                    "localField": "cnpj_ong",
                    "foreignField": "cnpj",
                    "as": "ong_details"
                }
            },
            {
                "$unwind": {
                    "path": "$ong_details",
                    "preserveNullAndEmptyArrays": True
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "titulo": 1,
                    "descricao": 1,
                    "data_inicio": 1,
                    "data_fim": 1,
                    "status": 1,
                    "meta": 1,
                    "comentario": 1,
                    "locais_arrecadacao": 1,
                    "cnpj_ong": 1,
                    "nome_ong": "$ong_details.nome"
                }
            }
        ]
        result = list(self.collection.aggregate(pipeline))
        return result

    def get_meta_doacoes_por_campanha(self, campanha_id):
        pipeline = [
            {
                "$match": {
                    "id": campanha_id
                }
            },
            {
                "$lookup": {
                    "from": "doacoes",
                    "localField": "id",
                    "foreignField": "id_campanha",
                    "as": "doacoes_detalhes"
                }
            },
            {
                "$unwind": {
                    "path": "$doacoes_detalhes",
                    "preserveNullAndEmptyArrays": True
                }
            },
            {
                "$match": {
                    "doacoes_detalhes.dinheiro": {"$ne": None}
                }
            },
            {
                "$group": {
                    "_id": "$id",
                    "titulo": {"$first": "$titulo"},
                    "descricao": {"$first": "$descricao"},
                    "meta": {"$first": "$meta"},
                    "comentarios": {"$first": "$comentario"},
                    "total_arrecadado": {"$sum": "$doacoes_detalhes.dinheiro"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "titulo": 1,
                    "descricao": 1,
                    "meta": 1,
                    "total_arrecadado": 1,
                    "comentarios": 1
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

    def find_many(self, query = ""):
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