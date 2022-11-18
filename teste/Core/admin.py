from django.contrib import admin
from .models import Cargo, Produtos, Servico, Funcionario, Saldo, User


admin.site.register(User)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'icone','ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo','ativo', 'modificado')
    search_fields = ('nome', 'cargo')

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco','descricao','imagem','estoque','ativo', 'modificado')
    search_fields = ('nome', 'preco', 'estoque')

@admin.register(Saldo)
class SaldoAdmin(admin.ModelAdmin):
    list_display = ('saldo', 'produto', 'modificado')

