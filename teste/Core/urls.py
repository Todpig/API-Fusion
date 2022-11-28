from django.urls import path
from Core.views import *

urlpatterns = [
    path("mostrar_saldo/", SaldoViewSet.as_view(), name="mostrar_saldo"),
    path("listar_servicos/", ServicosViewSet.as_view(), name="listar_servicos"),
    path("listar_produtos/", ProdutosViewSet.as_view(), name="listar_produtos"),
    path("listar_funcionario/",  FuncionarioViewSet.as_view(), name="listar_funcionario"),  
    path("login/",LoginViewSet.as_view()),
    path('', IndexView.as_view(), name='index'),
    path('index/<int:id>', atualiza_estoque, name="index"),
    path('listar_produtos/<int:pk>', ListaProdutosPorId.as_view(), name='listar_produtos_id'), 
   
]