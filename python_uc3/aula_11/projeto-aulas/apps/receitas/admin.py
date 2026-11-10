##
# APP: receitas - admin.py
##
# Importa o módulo de administração do Django.
# Ele fornece admin.site, o decorador @admin.register e a classe ModelAdmin.
from django.contrib import admin

# Importa os modelos que serão exibidos no painel administrativo.
# O ponto inicial indica importação relativa: estamos importando
# do arquivo models.py localizado na mesma aplicação.
from .models import Categoria, Receita


# Registra o modelo Categoria com a configuração padrão do Django Admin.
#admin.site.register(Categoria) # <-- Comentar (Aula 09)

# Registra o modelo Receita com a configuração padrão do Django Admin.
#admin.site.register(Receita) # <-- Comentar (Aula 09)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ["nome"]
    search_fields = ["nome"]
    ordering = ["nome"]


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    """Configuração administrativa para o modelo Receita."""

    list_display = [
        "titulo",
        "autor",
        "tempo_preparo",
        "publicada",
        "data_publicacao",
    ]
    
    list_filter = ["publicada", "categorias", "data_publicacao"]
    search_fields = ["titulo", "ingredientes", "modo_preparo"]
    filter_horizontal = ["categorias"]
    readonly_fields = ["data_publicacao", "autor"]
    ordering = ["-data_publicacao"]
    list_editable = ["publicada", "tempo_preparo"]