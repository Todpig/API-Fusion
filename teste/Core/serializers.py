from rest_framework import serializers
from .models import Funcionario, Produtos, Saldo, Servico, User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed, ParseError
from rest_framework_simplejwt.tokens import RefreshToken



class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome','cargo', 'ativo', 'bio')

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ('nome', 'preco', 'estoque')

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        exclude = ['icone']

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saldo
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['id','email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

      

        if not user:
            raise AuthenticationFailed('Credenciais erradas, tente novamente.')

        return {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens,
        }

