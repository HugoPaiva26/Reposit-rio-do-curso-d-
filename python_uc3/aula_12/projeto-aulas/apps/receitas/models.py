##
# APP: receitas - models.py
##
# importando o modelo de usuário do Django
from django.contrib.auth.models import User

from django.db import models


class Categoria(models.Model):
    """Representa uma categoria de receita, como Sobremesa ou Jantar."""

    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Receita(models.Model):
    """Representa uma receita publicada no sistema."""

    titulo = models.CharField(max_length=200)

    ingredientes = models.TextField(
        help_text="Informe um ingrediente por linha."
    )

    modo_preparo = models.TextField(
        help_text="Descreva o passo a passo do preparo."
    )

    tempo_preparo = models.PositiveIntegerField(
        help_text="Tempo total de preparo, em minutos."
    )

    data_publicacao = models.DateTimeField(auto_now_add=True)

    publicada = models.BooleanField(default=False)

    # Relação N:N: uma receita pode ter várias categorias
    # e uma categoria pode estar em várias receitas.
    categorias = models.ManyToManyField(
        Categoria,
        related_name="receitas",
        blank=True,
    )

    # Relação 1:N: cada receita pertence a um autor.
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="receitas",
    )

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ["-data_publicacao"]

    def __str__(self):
        return self.titulo