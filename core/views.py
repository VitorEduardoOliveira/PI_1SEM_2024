from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from core.forms import ONGForm
from core.models import ONGModel

def index(request):
  if request.method == "GET":
    return render(request, "index.html")
  return HttpResponseRedirect(reverse('core:index'))

def doe(request):
  if request.method == "GET":
    return render(request, "doe.html")
  return HttpResponseRedirect(reverse('core:doe'))

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
    form = ONGForm(request.POST)
    if form.is_valid():
      ONGModel.objects.create(**form.cleaned_data)
      return HttpResponseRedirect(reverse('core:login'))
    contexto = {'form': form}
    return render(request, "login.html", contexto)
  contexto = {'form': ONGForm()}
  return render(request, "login.html", contexto)