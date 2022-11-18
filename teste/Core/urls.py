from django.urls import path
from Core.views import *

urlpatterns = [
    path("listar_funcionario/",  FuncionarioViewSet.as_view(), name="listar_funcionario"),  
    path("login/",LoginViewSet.as_view()),
    path('', IndexView.as_view(), name='index'),
    path('index/<int:id>', atualiza_estoque, name="index"),

]