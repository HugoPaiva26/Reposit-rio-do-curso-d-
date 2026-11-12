from decimal import Decimal

from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True, #Impede duas categorias com o mesmo nome
        verbose_name="Nome",
        )
    descricao = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Descrição",
        )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

