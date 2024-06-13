# myapp/tests/test_doacoes_repository.py

import pytest

def test_insert_one(doacoes_repo):
    nova_doacao = {
        "id_campanha": 2,
        "alimento": "Arroz",
        "qtde": 20,
        "dinheiro": None,
        "id_doador": "D3"
    }
    id_inserido = doacoes_repo.insert_one(nova_doacao)
    assert id_inserido is not None

    # Verificando inserção
    doacao_inserida = doacoes_repo.find_one({"id_campanha": 2, "alimento": "Arroz"})
    assert doacao_inserida is not None
    assert doacao_inserida["alimento"] == "Arroz"

def test_find_one(doacoes_repo):
    query = {"id_campanha": 1, "alimento": "Feijão"}
    doacao = doacoes_repo.find_one(query)
    assert doacao is not None
    assert doacao["alimento"] == "Feijão"

def test_find_many(doacoes_repo):
    query = {"id_campanha": 1}
    doacoes = doacoes_repo.find_many(query)
    assert len(doacoes) > 0
    for doacao in doacoes:
        assert doacao["id_campanha"] == 1

def test_update_one(doacoes_repo):
    query = {"id_campanha": 1, "alimento": "Feijão"}
    update_values = {"qtde": 15}
    modified_count = doacoes_repo.update_one(query, update_values)
    assert modified_count == 1

    #Verificando update
    updated_doacao = doacoes_repo.find_one(query)
    assert updated_doacao["qtde"] == 15

def test_delete_one(doacoes_repo):
    query = {"id_campanha": 1, "alimento": "Feijão"}
    deleted_count = doacoes_repo.delete_one(query)
    assert deleted_count == 1

    # Verificando delete
    deleted_doacao = doacoes_repo.find_one(query)
    assert deleted_doacao is None

def test_delete_many(doacoes_repo):
    query = {"id_campanha": 1}
    deleted_count = doacoes_repo.delete_many(query)
    assert deleted_count > 0

    # Verificando delete many
    doacoes_excluidas = doacoes_repo.find_many(query)
    assert len(doacoes_excluidas) == 0 

def test_get_doacoes_alimento_por_campanha(doacoes_repo):
    id_campanha = 1
    alimentos = doacoes_repo.get_doacoes_alimento_por_campanha(id_campanha)
    assert len(alimentos) > 0
    for alimento in alimentos:
        assert alimento["alimento"] is not None

def test_get_doacoes_dinheiro_por_campanha(doacoes_repo):
    id_campanha = 2
    dinheiro = doacoes_repo.get_doacoes_dinheiro_por_campanha(id_campanha)
    assert len(dinheiro) == 1
    for doacao in dinheiro:
        assert doacao["dinheiro"] is not None

def test_get_alimento_mais_doado(doacoes_repo):
    result = doacoes_repo.get_alimento_mais_doado()
    assert len(result) > 0
    mais_doado = result[0]
    assert mais_doado["_id"] is not None
    assert mais_doado["_id"] == "Feijão"
    assert mais_doado["totalQuantity"] == 25

def test_get_alimento_mais_doado_por_campanha(doacoes_repo):
    id_campanha = 1
    result = doacoes_repo.get_alimento_mais_doado(id_campanha)
    assert len(result) > 0
    mais_doado = result[0]
    assert mais_doado["_id"] is not None
    assert mais_doado["_id"] == "Arroz"
    assert mais_doado["totalQuantity"] == 20
    
def test_get_total_alimentos(doacoes_repo):
    alimento = "Feijão"
    qtde_total = doacoes_repo.get_total_alimentos(alimento)
    assert qtde_total == 25
