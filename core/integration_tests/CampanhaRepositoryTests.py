# myapp/tests/test_campanha_repository.py

import pytest

def test_get_detalhes_campanha(campanha_repo):
    campanha_id = 1
    detalhes = campanha_repo.get_detalhes_campanha(campanha_id)
    assert len(detalhes) > 0
    campanha = detalhes[0]
    assert campanha["titulo"] == "Campanha 1"
    assert campanha["nome_ong"] == "ONG Exemplo"

def test_get_meta_doacoes_por_campanha(campanha_repo):
    campanha_id = 3
    metas_doacoes = campanha_repo.get_meta_doacoes_por_campanha(campanha_id)

    assert len(metas_doacoes) > 0
    campanha = metas_doacoes[0]
    assert campanha["titulo"] == "Campanha 3"
    assert campanha["total_arrecadado"] == 250

def test_insert_one(campanha_repo):
    nova_campanha = {
        "id": 4,
        "titulo": "Campanha 4",
        "descricao": "Descricao 4",
        "data_inicio": "2024-01-01",
        "data_fim": "2024-12-31",
        "status": "Ativa",
        "meta": 4000,
        "comentario": "Comentario 4",
        "locais_arrecadacao": [
            {"endereco": "Local 4", "horario_inicio": "08:00", "horario_termino": "18:00"}
        ],
        "cnpj_ong": "12.345.678/0001-99"
    }
    inserted_id = campanha_repo.insert_one(nova_campanha)
    assert inserted_id is not None

    # Verificando insert
    inserted_campanha = campanha_repo.find_one({"id": 4})
    assert inserted_campanha is not None
    assert inserted_campanha["titulo"] == "Campanha 4"

def test_find_one(campanha_repo):
    query = {"id": 1}
    campanha = campanha_repo.find_one(query)
    assert campanha is not None
    assert campanha["titulo"] == "Campanha 1"

def test_find_many(campanha_repo):
    query = {"status": "Ativa"}
    campanhas = campanha_repo.find_many(query)
    assert len(campanhas) > 0
    for campanha in campanhas:
        assert campanha["status"] == "Ativa"

def test_update_one(campanha_repo):
    query = {"id": 1}
    update_values = {"meta": 1500}
    modified_count = campanha_repo.update_one(query, update_values)
    assert modified_count == 1
    assert campanha_repo.find_one({"id": 1})["meta"] == 1500

    # Verificando update
    updated_campanha = campanha_repo.find_one(query)
    assert updated_campanha["meta"] == 1500

def test_delete_one(campanha_repo):
    query = {"id": 1}
    deleted_count = campanha_repo.delete_one(query)
    assert deleted_count == 1

    # verificando delete
    campanha_deletada = campanha_repo.find_one(query)
    assert campanha_deletada is None

def test_delete_many(campanha_repo):
    query = {"status": "Ativa"}
    deleted_count = campanha_repo.delete_many(query)
    assert deleted_count > 0

    # Verificando delete
    campanhas_restantes = campanha_repo.find_many(query)
    assert len(campanhas_restantes) == 0
