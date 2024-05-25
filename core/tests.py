import pytest
from django.urls import reverse
from core.models import ONGModel
from django.test import Client

@pytest.mark.django_db
def test_loginONG_valid_data():
    client = Client()
    url = reverse('core:loginONG')
    data = {
        'name': 'Test ONG',
        'email': 'test@ong.com',
        'password': 'password123'
    }
    response = client.post(url, data)
    
    # Verifica se a ONG foi criada
    assert ONGModel.objects.count() == 1
    
    # Verifica o redirecionamento
    assert response.status_code == 302
    assert response.url == reverse('core:login')

@pytest.mark.django_db
def test_loginONG_invalid_data():
    client = Client()
    url = reverse('core:loginONG')
    data = {
        'name': '',  # Campo obrigatório não preenchido
        'email': 'invalid-email',
        'password': 'password123'
    }
    response = client.post(url, data)
    
    # Verifica se a ONG não foi criada
    assert ONGModel.objects.count() == 0
    
    # Verifica se a resposta é 200 (a página de login é renderizada novamente com erros)
    assert response.status_code == 200
    assert 'form' in response.context
    assert response.context['form'].errors

@pytest.mark.django_db
def test_loginONG_get_request():
    client = Client()
    url = reverse('core:loginONG')
    response = client.get(url)
    
    # Verifica se a página de login é renderizada corretamente
    assert response.status_code == 200
    assert 'form' in response.context