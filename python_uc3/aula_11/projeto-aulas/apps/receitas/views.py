##
# APP: receitas - views.py
##
from django.shortcuts import render, get_object_or_404

# Importando o modelo de Receita para poder buscar as receitas no banco de dados
from .models import Receita


def lista_receitas(request):
    receitas = Receita.objects.filter(publicada=True)
    context = {
        "receitas": receitas,
    }
    return render(request, "receitas/listar_receitas-table.html", context)


def exibir_receita(request, pk):
    """
    Exibe os detalhes de uma receita específica.

    O parâmetro 'pk' vem da URL dinâmica:
    /receita/<int:pk>/
    """

    # Busca a receita pelo ID e exige que ela esteja publicada.
    # Se não existir, o Django retorna automaticamente um erro 404.
    receita = get_object_or_404(
        Receita,
        pk=pk,
        publicada=True,
    )

    context = {
        "receita": receita,
    }

    return render(request, "receitas/detalhe-full.html", context)