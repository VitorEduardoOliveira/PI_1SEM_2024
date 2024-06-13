from django import forms
from django.core.exceptions import ValidationError

class ONGForm(forms.Form):
  Nome = forms.CharField(max_length=50)
  Telefone = forms.CharField(max_length=15)
  Email = forms.EmailField(max_length=100)
  Senha = forms.CharField(max_length=128, widget=forms.PasswordInput)
  CNPJ = forms.CharField(max_length=15)

  def clean_nome(self):
    nome = self.cleaned_data.get['Nome']
    return nome.title()

  def clean_telefone(self):
    telefone = self.cleaned_data.get['Telefone']
    if len(telefone) == 11:
      return telefone
    raise ValidationError('Número de Telefone invávlido')

  def clean_email(self):
    email = self.cleaned_data.get['Email']
    return email
  
  def clean_cnpj(self):
    cnpj = self.cleaned_data["CNPJ"]
    if len(cnpj) == 11:
      return cnpj
    raise ValidationError('tem que ter 11 caracteres')
  
  def clean_senha(self):
    senha = self.cleaned_data["senha"]
    return senha
    
class ONGLoginForm(forms.Form):
  CNPJ = forms.CharField(max_length=15)
  Senha = forms.CharField(max_length=128, widget=forms.PasswordInput)
  
  def clean_cnpj(self):
    cnpj = self.cleaned_data["CNPJ"]
    if len(cnpj) == 11:
      return cnpj
    raise ValidationError('tem que ter 11 caracteres')
  
  def clean_senha(self):
    senha = self.cleaned_data["senha"]
    return senha
  
class PubliONGForm(forms.Form): 
  Mensagem = forms.CharField(max_length=1028, widget=forms.Textarea)
  Meta = forms.FloatField()
  Nome = forms.CharField(max_length=50)
  DataExpiracao = forms.DateField()
  Locais = forms.CharField()
  
  def clean_mensagem(self):
    mensagem = self.cleaned_data["mensagem"]
    return mensagem
  
  def clean_metaArrecadacao(self):
    metaArrecadacao = self.cleaned_data["metaArrecadacao"]
    if metaArrecadacao > 0:
      return metaArrecadacao
    return ValidationError("tem que ser um valor positivo")
  
  def clean_nome(self):
    nome = self.cleaned_data["nome"]
    return nome.title()
  
  def clean_dataExpiracao(self):
    dataExpi = self.cleaned_data["dataExpi"]
    return dataExpi
  
  def clean_locaisAjuda(self):
    locais = self.cleaned_data["locais"]
    return locais
  

class DoacaoForm(forms.Form):
  Nome = forms.CharField(max_length=15)
  Data = forms.DateField()
  Valor = forms.CharField(max_length=10)
    
  def clean_nome(self):
    nome = self.cleaned_data['Nome']
    return nome.title()
  
  def clean_data(self):
    data = self.cleaned_data["Data"]
    return data

  def clean_valor(self):
    valor = self.cleaned_data["Valor"]
    return valor
  
class ValidacaoForm(forms.Form):
  Nome_Cartao = forms.CharField(max_length=70)
  Num_Cartao = forms.CharField(max_length=50)
  Mes_Cartao = forms.IntegerField()
  Ano_Cartao = forms.IntegerField()
  CVV = forms.IntegerField()
  
  def clean_nome_cart(self):
    nome_cart = self.cleaned_data["nome_cart"]
    return nome_cart
  
  def clean_num_cart(self):
    num_cart = self.cleaned_data["num_cart"]
    return num_cart
  
  def clean_ano_cart(self):
    ano_cart = self.cleaned_data["ano_cart"]
    return ano_cart
  
  def clean_mes_cart(self):
    mes_cart = self.cleaned_data["mes_cart"]
    return mes_cart
  
  def clean_cvv(self):
    cvv = self.cleaned_data["cvv"]
    return cvv
  