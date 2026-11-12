##
# APP: receitas - urls.py
##
from django.urls import path

from . import views

# Nome do namespace da aplicação.
# Permite usar, por exemplo: {% url 'receitas:detalhe_receita' receita.pk %}
app_name = "receitas"

urlpatterns = [
    # Página inicial: lista todas as receitas publicadas
    path("", views.lista_receitas, name="listar_receitas"),

    # URL dinâmica:
    # <int:pk> captura um número inteiro e o envia à view como parâmetro 'pk'
    path("receita/<int:pk>/",views.exibir_receita,name="exibir_receita" ),
]