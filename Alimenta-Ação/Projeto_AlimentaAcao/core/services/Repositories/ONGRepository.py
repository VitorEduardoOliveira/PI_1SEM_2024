import hashlib
from core.services.MongoService import MongoService

class ONGRepository:
    def __init__(self, mongo_service: MongoService):
        self.db = mongo_service.db
        self.collection = self.db["ongs"]
        
    def validar_cnpj(self, cnpj):
        document = self.collection.count_documents({'CNPJ': cnpj})
        if document >= 1:
            return False
        return True

    def insert_one(self, document):
        document["Senha"] = self.hash_password(document["Senha"])
        result = self.collection.insert_one(document)
        return result.inserted_id

    def find_one(self, query):
        document = self.collection.find_one(query)
        return document

    def find_many(self, query = ""):
        documents = self.collection.find(query)
        return list(documents)

    def update_one(self, query, update_values):
        if "Senha" in update_values:
            update_values["Senha"] = self.hash_password(update_values["Senha"])
        result = self.collection.update_one(query, {"$set": update_values})
        return result.modified_count

    def delete_one(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count

    def delete_many(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count
    
    def login(self, cnpj, senha):
        hash_senha = self.hash_password(senha)
        query = {"CNPJ": cnpj, "Senha": hash_senha}
        user = self.find_one(query)
        return user
    
    def get_ONGS_detalhes(self, cnpj):
        pipeline = [
            {
                "$match": {
                    "cnpj": cnpj
                }
            },
            {
                "$lookup": {
                    "from": "campanhas",
                    "localField": "cnpj",
                    "foreignField": "cnpj_ong",
                    "as": "campanhas_detalhes"
                }
            },
            {
                "$unwind": {
                    "path": "$campanhas_detalhes",
                    "preserveNullAndEmptyArrays": True
                }
            },
            {
                "$group": {
                    "_id": "$cnpj",
                    "nome": { "$first": "$nome" },
                    "enderecos": { "$first": "$endereco" },
                    "email": { "$first": "$email" },
                    "links": { "$first": "$links" },
                    "campanhas": { "$push": "$campanhas_detalhes.titulo" }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "cnpj": "$_id",
                    "nome": 1,
                    "enderecos": 1,
                    "email": 1,
                    "links": 1,
                    "campanhas": 1
                }
            }
        ]
        result = list(self.collection.aggregate(pipeline))
        return result

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()