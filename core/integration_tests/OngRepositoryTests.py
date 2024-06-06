# myapp/tests/test_ong_repository.py

import pytest

def test_insert_one(ong_repo):
    new_ong = {
        "cnpj": "98.765.432/0001-10",
        "nome": "Nova ONG",
        "endereco": "456 Rua Fatec, Araras, Brazil",
        "telefone": "+987654321",
        "email": "contact@newong.org",
        "links": ["http://newong.org", "http://facebook.com/newong"],
        "senha": "senhasegura",
        "cidades_cobertura": ["Araras", "Leme"]
    }
    inserted_id = ong_repo.insert_one(new_ong)
    assert inserted_id is not None

    # Verificando Insert
    inserted_ong = ong_repo.find_one({"cnpj": "98.765.432/0001-10"})
    assert inserted_ong is not None
    assert inserted_ong["nome"] == "Nova ONG"

def test_find_one(ong_repo):
    query = {"cnpj": "12.345.678/0001-99"}
    ong = ong_repo.find_one(query)
    assert ong is not None
    assert ong["nome"] == "ONG Exemplo"

def test_find_many(ong_repo):
    query = {"cidades_cobertura": "Araras"}
    ongs = ong_repo.find_many(query)
    assert len(ongs) == 2
    for ong in ongs:
        assert "Araras" in ong["cidades_cobertura"]

def test_update_one(ong_repo):
    query = {"cnpj": "12.345.678/0001-99"}
    update_values = {"telefone": "+987654321"}
    modified_count = ong_repo.update_one(query, update_values)
    assert modified_count == 1

    # Verificando update
    updated_ong = ong_repo.find_one(query)
    assert updated_ong["telefone"] == "+987654321"

def test_delete_one(ong_repo):
    query = {"cnpj": "12.345.678/0001-99"}
    deleted_count = ong_repo.delete_one(query)
    assert deleted_count == 1

    # Verificando delete
    deleted_ong = ong_repo.find_one(query)
    assert deleted_ong is None

def test_delete_many(ong_repo, test_db):
    query = {"cidades_cobertura": "Araras"}
    deleted_count = ong_repo.delete_many(query)
    assert deleted_count == 2

    # Verificando delete
    ongs_restantes = ong_repo.find_many()
    assert len(ongs_restantes) == 1

def test_login(ong_repo):
    cnpj = "12.345.678/0001-99"
    senha = "senhasegura"
    login_success = ong_repo.login(cnpj, senha)
    assert login_success

    # Teste com senha errada
    senha_errada = ong_repo.login(cnpj, "senhaerrada")
    assert not senha_errada

def test_get_ONGS_detalhes(ong_repo):
    cnpj = "12.345.678/0001-99"
    result = ong_repo.get_ONGS_detalhes(cnpj)
    assert len(result) > 0
    ong_com_campanhas = result[0]
    assert ong_com_campanhas["cnpj"] == cnpj
    assert "Campanha 1" in ong_com_campanhas["campanhas"]
