# Generated by Django 4.1.3 on 2022-11-18 00:32

import Core.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cargo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "criados",
                    models.DateField(auto_now_add=True, verbose_name="Criação"),
                ),
                (
                    "modificado",
                    models.DateField(auto_now=True, verbose_name="Atualização"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("cargo", models.CharField(max_length=100, verbose_name="Cargo")),
            ],
            options={
                "verbose_name": "Cargo",
                "verbose_name_plural": "Cargos",
            },
        ),
        migrations.CreateModel(
            name="Produtos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "criados",
                    models.DateField(auto_now_add=True, verbose_name="Criação"),
                ),
                (
                    "modificado",
                    models.DateField(auto_now=True, verbose_name="Atualização"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "descricao",
                    models.TextField(max_length=200, verbose_name="Descrição"),
                ),
                ("preco", models.IntegerField(null=True, verbose_name="Preço")),
                (
                    "imagem",
                    stdimage.models.StdImageField(
                        force_min_size=False,
                        null=True,
                        upload_to=Core.models.get_file_path,
                        variations={},
                        verbose_name="Imagem",
                    ),
                ),
                ("estoque", models.IntegerField(null=True, verbose_name="Estoque")),
            ],
            options={
                "verbose_name": "Produto",
                "verbose_name_plural": "Produtos",
            },
        ),
        migrations.CreateModel(
            name="Servico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "criados",
                    models.DateField(auto_now_add=True, verbose_name="Criação"),
                ),
                (
                    "modificado",
                    models.DateField(auto_now=True, verbose_name="Atualização"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("servicos", models.CharField(max_length=100, verbose_name="Serviço")),
                (
                    "descricao",
                    models.TextField(max_length=200, verbose_name="Descrição"),
                ),
                (
                    "icone",
                    models.CharField(
                        choices=[
                            ("lni-cog", "Engrenagem"),
                            ("lni-stats-up", "Gráfico"),
                            ("lni-users", "Usuários"),
                            ("lni-layers", "Design"),
                            ("lni-mobile", "Mobile"),
                            ("lni-rocket", "Foguete"),
                        ],
                        max_length=12,
                        verbose_name="Icone",
                    ),
                ),
            ],
            options={
                "verbose_name": "Serviço",
                "verbose_name_plural": "Serviços",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="Nome Usuário"
                    ),
                ),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=255, unique=True),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário",
            },
        ),
        migrations.CreateModel(
            name="Saldo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "criados",
                    models.DateField(auto_now_add=True, verbose_name="Criação"),
                ),
                (
                    "modificado",
                    models.DateField(auto_now=True, verbose_name="Atualização"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                (
                    "saldo",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=30),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Core.produtos",
                    ),
                ),
            ],
            options={
                "verbose_name": "Saldo",
                "verbose_name_plural": "Saldos",
            },
        ),
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "criados",
                    models.DateField(auto_now_add=True, verbose_name="Criação"),
                ),
                (
                    "modificado",
                    models.DateField(auto_now=True, verbose_name="Atualização"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                ("bio", models.TextField(max_length=200, verbose_name="Bio")),
                (
                    "imagem",
                    stdimage.models.StdImageField(
                        force_min_size=False,
                        null=True,
                        upload_to=Core.models.get_file_path,
                        variations={},
                        verbose_name="Imagem",
                    ),
                ),
                (
                    "facebook",
                    models.CharField(
                        default="#", max_length=100, verbose_name="Facebook"
                    ),
                ),
                (
                    "twitter",
                    models.CharField(
                        default="#", max_length=100, verbose_name="Twitter"
                    ),
                ),
                (
                    "instagram",
                    models.CharField(
                        default="#", max_length=100, verbose_name="Instagram"
                    ),
                ),
                (
                    "cargo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Core.cargo",
                        verbose_name="Cargo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Funcionário",
                "verbose_name_plural": "Funcionários",
            },
        ),
    ]
