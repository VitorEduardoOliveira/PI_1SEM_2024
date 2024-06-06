from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('doe/', views.doe, name='doe'),
    path('nossotime/', views.nossotime, name='nossotime'),
    path('entreemcontato', views.contato, name='contato'),
    path('avaliacao/', views.avaliacao, name='avaliacao'),
    path('login/', views.loginONG, name='login'),
    # path('recuperacaologin/'),
]
