##
# paginas - views.py
##
# importando o módulo de mensagens do Django
from django.contrib import messages
#
from django.shortcuts import render

# Página Principal
def home(request):    
    #messages.success(request, "pages criado com sucesso!")
    return render(
        request,
        "paginas/home.html",
        {"titulo": "Página Inicial"},
    )

# Página Sobre
def sobre(request):    
    return render(
        request,
        "paginas/sobre.html",
        {"titulo": "Sobre Nós"},
    )

# Página com a Política de Privacidade
def politica_privacidade(request):
    return render(
        request,
        "paginas/politica_privacidade.html",
        {"titulo": "Política de Privacidade"},
    )

# Página de Contato
def contato(request):
    return render(
        request,
        "paginas/contato.html",
        {"titulo": "Contato"},
    )

# Página de Quem Somos
def quem_somos(request):
    return render(
        request,
        "paginas/quem_somos.html",
        {"titulo": "Conheça um pouco mais sobre nós"},
    )

# Página de Termos de Uso
def termos_de_uso(request):
    return render(
        request,
        "paginas/termos_de_uso.html",
        {"titulo": "Termos de Uso"},
    )

# Página para Anunciar
def anuncie(request):
    return render(
        request,
        "paginas/anuncie.html",
        {"titulo": "Anuncie Aqui !!!"},
    )