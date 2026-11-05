##
# paginas - urls.py
##
from django.urls import path
from . import views     # Importando as views da aplicação de páginas estáticas

app_name = 'paginas'  # Cria um namespace para as urls da aplicação de páginas estáticas

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path(
        "politica-privacidade/",
        views.politica_privacidade,
        name="politica_privacidade",
    ),
    path("contato/", views.contato, name="contato"),
]
