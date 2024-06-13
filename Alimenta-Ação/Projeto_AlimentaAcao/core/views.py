from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from core.forms import ONGForm, ONGLoginForm, PubliONGForm, DoacaoForm, ValidacaoForm
from .services.Repositories.ONGRepository import ONGRepository
from .services.Repositories.DoacaoRepository import DoacaoRepository
from .services.Repositories.CampanhaRepository import CampanhaRepository
from .services.ConnectionService import ConnectionService
from .services.MongoService import MongoService
from django.contrib import messages
from bson.objectid import ObjectId
import datetime

def index(request):
  if request.method == "GET":
    conexao = ConnectionService()
    banco = MongoService(conexao, "AlimentaAcao")
    repository = CampanhaRepository(banco)
    campanha = {
      'campanhas': repository.find_many({})
    }
    print(campanha)
    return render(request, "index.html", campanha)
  return HttpResponseRedirect(reverse('core:index'))

def doe(request):
  id = request.GET.get('id')
  conexao = ConnectionService()
  banco = MongoService(conexao, "AlimentaAcao")
  repositoryDoa = DoacaoRepository(banco)
  repositoryCamp = CampanhaRepository(banco)
  
  campanha = repositoryCamp.find_one({'_id': ObjectId(id)})
  if request.method == "POST":
    form = DoacaoForm(request.POST)
    if form.is_valid():
      query = {
        'doador': form.cleaned_data.get('Nome'),
        'valor': form.cleaned_data.get('Valor'),
        'data_envio': str(form.cleaned_data.get('Data'))
      }
      repositoryDoa.insert_one(query)
      doar = repositoryDoa.find_one(query)
    return HttpResponseRedirect(f'{reverse('core:validacao')}?id={doar['_id']}')
  contexto = {
    'titulo': campanha['titulo'],
    'descricao': campanha['descricao'],
    'locais': campanha['locais'],
  }
  return render(request, "doe.html", contexto)

def doacao(request):
  id = request.GET.get('id')
  conexao = ConnectionService()
  banco = MongoService(conexao, "AlimentaAcao")
  repository = DoacaoRepository(banco)
  query = {
    '_id': ObjectId(id)
  }
  if request.method == "POST":
    form = ValidacaoForm(request.POST)
    print(form.is_valid())
    if 'validar' in request.POST:
      if form.is_valid():
        valores = {
          "Nome_Cartao": form.cleaned_data.get('Nome_Cartao'),
          "Num_Cartao": form.cleaned_data.get('Num_Cartao'),
          "Mes_Cartao": form.cleaned_data.get('Mes_Cartao'),
          "Ano_Cartao": form.cleaned_data.get('Ano_Cartao'),
          "CVV": form.cleaned_data.get('CVV'),
          'id_campanha': id,
        }
        print(query)
        print(valores)
        repository.update_one(query, valores)
        return HttpResponseRedirect(reverse('core:validacaocon'))
    elif 'cancelar' in request.POST:
      repository.delete_one(query)
      return HttpResponseRedirect(reverse('core:validacaocon'))
  doador = repository.find_one(query)
  contexto = {
    "DoacaoForm": ValidacaoForm(),
    'valor': doador['valor'],
  }
  return render(request, "validacao.html", contexto)

def validacaoCon(request):
  if request.method == "GET":
    return render(request, "validacaoconcluida.html")
  return HttpResponseRedirect(reverse('core:validacaocon'))
  
def nossotime(request):
  if request.method == "GET":
    return render(request, "nossotime.html")
  return HttpResponseRedirect(reverse('core:nossotime'))

def contato(request):
  if request.method == "GET":
    return render(request, "contato.html")
  return HttpResponseRedirect(reverse('core:contato'))

def avaliacao(request):
  if request.method == "GET":
    return render(request, "avaliacao.html")
  return HttpResponseRedirect(reverse('core:avaliacao'))

def loginONG(request):
  if request.method == "POST":
    if 'cadastro-submit' in request.POST:
      form = ONGForm(request.POST)
      if form.is_valid():
        conexao = ConnectionService()
        banco = MongoService(conexao, "AlimentaAcao")
        repository = ONGRepository(banco)
        existe = repository.validar_cnpj(form.cleaned_data.get('CNPJ'))
        if existe:
          repository.insert_one(form.cleaned_data)
          usuario = repository.login(form.cleaned_data.get('CNPJ'), form.cleaned_data.get('Senha'))
          if usuario is not None:
            id = usuario['_id']
            return HttpResponseRedirect(f'{reverse('core:indexong')}?id={id}')
          else:
            messages.success(request, "CNPJ ou Senha inválido!!")
        else:
          messages.success(request, "Esse usuário já existe, tente novamente!!!")
    elif 'login-submit' in request.POST:
      form = ONGLoginForm(request.POST)
      if form.is_valid():
        conexao = ConnectionService()
        banco = MongoService(conexao, "AlimentaAcao")
        repository = ONGRepository(banco)
        usuario = repository.login(form.cleaned_data.get('CNPJ'), form.cleaned_data.get('Senha'))
        if usuario is not None:
          id = usuario['_id']
          return HttpResponseRedirect(f'{reverse('core:indexong')}?id={id}')
        else:
          messages.success(request, "CNPJ ou Senha inválido!!")
  contexto = {
    'cadastro_form': ONGForm(),
    'login_form': ONGLoginForm(),
  }
  return render(request, "login.html", contexto)

def indexOng(request):
  id = request.GET.get('id')
  conexao = ConnectionService()
  banco = MongoService(conexao, "AlimentaAcao")
  repositoryOng = ONGRepository(banco)

  ong = repositoryOng.find_one({'_id': ObjectId(id)})
  contexto = {
    'nome_ong': ong['Nome'],
    'id': ong['_id'],
  }
  return render(request, "indexong.html", contexto)

def paginaONG(request):
  id = request.GET.get('id')
  conexao = ConnectionService()
  banco = MongoService(conexao, "AlimentaAcao")
  repositoryOng = ONGRepository(banco)
  repositoryPubl = CampanhaRepository(banco)
  
  Ong = repositoryOng.find_one({'_id': ObjectId(id)})
  if Ong is not None:
    if request.method == 'POST':
      form = PubliONGForm(request.POST)
      if form.is_valid():
        cidades = form.cleaned_data.get('Locais')
        locais = cidades.split(",")
        query = {
          'titulo': form.cleaned_data.get('Nome'),
          'meta': float(form.cleaned_data.get('Meta')),
          'data_inicio': str(datetime.date.today()),
          'data_fim': str(form.cleaned_data.get('DataExpiracao')),
          'locais': locais,
          'descricao': form.cleaned_data.get('Mensagem'),
          'CNPJ_Ong': Ong['CNPJ'],
          'status': True,
        }
        repositoryPubl.insert_one(query)
    contexto = {
      'campanha_form': PubliONGForm(),
      'email': Ong['Email'],
      'telefone': Ong['Telefone']
    }
    return render(request, "publicarong.html", contexto)
  else:
    return HttpResponseRedirect(reverse('core:index'))
  
def ModificaCampanha(request):
  id = request.GET.get('id')
  conexao = ConnectionService()
  banco = MongoService(conexao, "AlimentaAcao")
  repository = CampanhaRepository(banco)
  repositoryOng = ONGRepository(banco)
  repositoryDoa = DoacaoRepository(banco)
  
  ong = repositoryOng.find_one({'_id': ObjectId(id)})
  campanha = repository.find_one({'CNPJ_Ong': ong['CNPJ']})
  if request.method == "GET":
    campanha = {
      'campanhas': repository.find_many({}),
      'nome_ong': ong['Nome'],
    }
    return render(request, "modificar.html", campanha)
  elif request.method == "POST":
    if 'editar' in request.POST:
      HttpResponseRedirect(f'{reverse('core:atualiza')}?id={campanha['_id']}')
    elif 'deletar' in request.POST:
      repository.delete_one({'_id': campanha['_id']})
      repositoryDoa.delete_many({'id_campanha': campanha['_id']})
      
  return HttpResponseRedirect(f'{reverse('core:modifica')}?id={id}')

def atualizar(request):
  id = request.GET.get('id')
  conexao = ConnectionService()
  banco = MongoService(conexao, "AlimentaAcao")
  repositoryOng = ONGRepository(banco)
  repositoryPubl = CampanhaRepository(banco)
  query = {
    '_id': ObjectId(id)
  }
  
  Publi = repositoryPubl.find_one(query)
  if Ong is not None:
    if request.method == 'POST':
      form = PubliONGForm(request.POST)
      if form.is_valid():
        cidades = form.cleaned_data.get('Locais')
        locais = cidades.split(",")
        valores = {
          'titulo': form.cleaned_data.get('Nome'),
          'meta': float(form.cleaned_data.get('Meta')),
          'data_fim': str(form.cleaned_data.get('DataExpiracao')),
          'locais': locais,
          'descricao': form.cleaned_data.get('Mensagem'),
        }
        repositoryPubl.update_one(query, valores)
  else:
    return HttpResponseRedirect(f'{reverse('core:modifica')}?id={Publi['id_campanha']}')
  contexto = {
    'titulo': Publi['titulo'],
    'meta': Publi['meta'],
    'data_fim': Publi['data_fim'],
    'locais': Publi['locais'],
    'descricao': Publi['descricao']
  }
  return render(request, "atualiza.html", contexto)