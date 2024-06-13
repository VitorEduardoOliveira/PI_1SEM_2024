# myapp/tests/conftest.py

import pytest
import pymongo
from pymongo import MongoClient
from core.services.MongoService import MongoService
from core.services.ConnectionService import ConnectionService
from core.services.repositories.ONGRepository import ONGRepository
from core.services.repositories.DoacaoRepository import DoacaoRepository
from core.services.repositories.CampanhaRepository import CampanhaRepository

@pytest.fixture(scope="module")
def mongo_client():
    client = MongoClient("mongodb://localhost:27017/")
    yield client
    client.close()

@pytest.fixture(scope="module")
def test_db(mongo_client):
    db = mongo_client["testdatabase"]
    yield db
    mongo_client.drop_database("testdatabase")

@pytest.fixture(scope="module")
def mongo_service(test_db):
    return MongoService(ConnectionService(), "testdatabase")

@pytest.fixture(scope="module")
def ong_repo(mongo_service):
    return ONGRepository(mongo_service)

@pytest.fixture(scope="module")
def doacoes_repo(mongo_service):
    return DoacaoRepository(mongo_service)

@pytest.fixture(scope="module")
def campanha_repo(mongo_service):
    return CampanhaRepository(mongo_service)

@pytest.fixture(scope="function", autouse=True)
def setup_default_data(test_db):
    default_ongs = [
        {
            "cnpj": "12.345.678/0001-99",
            "nome": "ONG Exemplo",
            "endereco": "123 Main St, City, Country",
            "telefone": "+123456789",
            "email": "contact@ongexample.org",
            "links": ["http://ongexample.org", "http://facebook.com/ongexample"],
            "senha": "0b940d0a0d32b3b405b33cf51c503bf04aa2db8afcf4f11a8de9b3568583b781",
            "cidades_cobertura": ["Araras", "Leme", "Limeira"]
        },
        {
            "cnpj": "98.765.432/0001-00",
            "nome": "ONG do Amor",
            "endereco": "456 Another St, Another City, Country",
            "telefone": "+987654321",
            "email": "contact@secondong.org",
            "links": ["http://secondong.org", "http://facebook.com/secondong"],
            "senha": "aa77b12e7007e4e023d91ec709c426cbce01c909c06846c6ef31deec10fa9e29",
            "cidades_cobertura": ["Campinas", "Araras"]
        },
        {
            "cnpj": "11.111.111/0001-11",
            "nome": "ONG Terciaria",
            "endereco": "789 Third St, Third City, Country",
            "telefone": "+111111111",
            "email": "contact@thirdong.org",
            "links": ["http://thirdong.org", "http://facebook.com/thirdong"],
            "senha": "aec342fb38b8173b8e898229990ed6a4f196d9bed8428f6d2b5a7010fe85781b",
            "cidades_cobertura": ["Leme", "Limeira"]
        }
    ]
    default_doacoes = [
        {
            "id_campanha": 1,
            "alimento": "Feijão",
            "qtde": 10,
            "dinheiro": None,
            "id_doador": "D1"
        },
        {
            "id_campanha": 1,
            "alimento": "Arroz",
            "qtde": 20,
            "dinheiro": None,
            "id_doador": "D2"
        },
        {
            "id_campanha": 2,
            "alimento": "Feijão",
            "qtde": 15,
            "dinheiro": None,
            "id_doador": "D3"
        },
        {
            "id_campanha": 2,
            "alimento": None,
            "qtde": 0,
            "dinheiro": 50.0,
            "id_doador": "D4"
        },
        {
            "id_campanha": 3,
            "alimento": None,
            "qtde": 0,
            "dinheiro": 100.0,
            "id_doador": "D5"
        },
        {
            "id_campanha": 3,
            "alimento": None,
            "qtde": 0,
            "dinheiro": 150.0,
            "id_doador": "D6"
        }
    ]
    default_campanhas = [
        {
            "id": 1,
            "titulo": "Campanha 1",
            "descricao": "Descricao 1",
            "data_inicio": "2023-01-01",
            "data_fim": "2023-12-31",
            "status": "Ativa",
            "meta": 1000,
            "comentario": "Comentario 1",
            "locais_arrecadacao": [
                {"endereco": "Local 1", "horario_inicio": "08:00", "horario_termino": "18:00"}
            ],
            "cnpj_ong": "12.345.678/0001-99"
        },
        {
            "id": 2,
            "titulo": "Campanha 2",
            "descricao": "Descricao 2",
            "data_inicio": "2023-02-01",
            "data_fim": "2023-12-31",
            "status": "Ativa",
            "meta": 2000,
            "comentario": "Comentario 2",
            "locais_arrecadacao": [
                {"endereco": "Local 2", "horario_inicio": "09:00", "horario_termino": "17:00"}
            ],
            "cnpj_ong": "98.765.432/0001-00"
        },
        {
            "id": 3,
            "titulo": "Campanha 3",
            "descricao": "Descricao 3",
            "data_inicio": "2023-03-01",
            "data_fim": "2023-12-31",
            "status": "Ativa",
            "meta": 3000,
            "comentario": "Comentario 3",
            "locais_arrecadacao": [
                {"endereco": "Local 3", "horario_inicio": "10:00", "horario_termino": "16:00"}
            ],
            "cnpj_ong": "11.111.111/0001-11"
        }
    ]

    test_db.ongs.insert_many(default_ongs)
    test_db.doacoes.insert_many(default_doacoes)
    test_db.campanhas.insert_many(default_campanhas)

    yield

    test_db.ongs.delete_many({})
    test_db.doacoes.delete_many({})
    test_db.campanhas.delete_many({})
