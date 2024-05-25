from django import forms
from django.core.exceptions import ValidationError

class ONGForm(forms.Form):
  Nome = forms.CharField(max_length=50)
  Telefone = forms.CharField(max_length=15)
  Email = forms.EmailField(max_length=50)
  Senha = forms.CharField(max_length=128, widget=forms.PasswordInput)
  Descricao = forms.CharField(max_length=254, widget=forms.Textarea)
  CNPJ = forms.CharField(max_length=15)

  def clean_nome(self):
    nome = self.cleaned_data.get['nome']
    return nome.title()

  def clean_telefone(self):
    telefone = self.cleaned_data.get['telefone']
    if len(telefone) == 11:
      return telefone
    raise ValidationError('Número de Telefone invávlido')

  def clean_email(self):
    email = self.cleaned_data.get['email']
    return email
  
  def clean_descriacao(self):
    descricao = self.cleaned_data["descriacao"]
    return descricao
  
  def clean_cnpj(self):
    cnpj = self.cleaned_data["cnpj"]
    if len(cnpj) == 11:
      return cnpj
    raise ValidationError('tem que ter 11 caracteres')
  
  