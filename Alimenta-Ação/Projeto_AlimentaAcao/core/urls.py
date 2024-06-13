from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('doe', views.doe, name='doe'),
    path('nossotime/', views.nossotime, name='nossotime'),
    path('entreemcontato', views.contato, name='contato'),
    path('avaliacao/', views.avaliacao, name='avaliacao'),
    path('login/', views.loginONG, name='login'),
    path('doe/validacao',views.doacao, name='validacao'),
    path('doe/validacao/concluida', views.validacaoCon, name='validacaocon'),
    # path('recuperacaologin/'),
    path('indexOng/publicacao', views.paginaONG, name='ong'),
    path('indexOng', views.indexOng, name='indexong'),
    path('indexOng/ModificarPublicacao', views.ModificaCampanha, name='modifica'),
    path('indexOng/ModificarPublicacao/atualizar', views.atualizar, name='atualiza'),
]
