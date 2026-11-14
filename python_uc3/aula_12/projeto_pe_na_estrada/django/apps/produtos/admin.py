from django.contrib import admin

# Register your models here.

from .models import (
    Categoria, 
    Produto, 
    Cliente, 
    EnderecoEntrega, 
    Pedido, 
    ItemPedido,
    ComentarioAvaliacao
)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para Categoria.
    """

    # Colunas exibidas na listagem.
    list_display = [
                    "id",
                    "nome", 
                    "descricao", 
                    ]

    # Campos pesquisáveis na caixa de busca.
    search_fields = ["nome"]

    # Ordenação padrão da listagem.
    ordering = ["nome"]

@admin.register(Produto)
class ProdutoAdmin (admin.ModelAdmin):
    list_display = [
        "categoria",
        "nome",
        "preco",
        "quantidade_estoque",
        "criado_em",
    ]
    search_fields = [
        "nome", 
        "descricao",
        "usuario",
        "cpf",
    ]

    ordering = ["nome"]
    
    

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    # Colunas exibidas na listagem.
    list_display = ["id", 
                    "usuario",
                    "telefone",
                    "sexo",
                    "nome_social",
                    "cpf",
                ]

    # Campos pesquisáveis na caixa de busca.
    search_fields = ["nome", 
                     "descricao",
                     "usuario",
                     "cpf",
                    ]

    # Ordenação padrão da listagem.
    ordering = ["usuario"]

@admin.register(EnderecoEntrega)
class EnderecoEntregaAdmin (admin.ModelAdmin):
     # Colunas exibidas na listagem.
        list_display = ["id", 
                        "cliente",
                        "cidade",
                        "estado",
                    ]
    
        # Campos pesquisáveis na caixa de busca.
        search_fields = ["cliente", 
                         "cidade",
                         "estado",
                        ]
    
        # Ordenação padrão da listagem.
        ordering = ["cliente"]

@admin.register(Pedido)
class PedidoAdmin (admin.ModelAdmin):
        
        # Colunas exibidas na listagem.
        list_display = ["id", 
                        "cliente",
                        "status",
                        "criado_em",
                    ]
    
        # Campos pesquisáveis na caixa de busca.
        search_fields = ["cliente", 
                         "criado_em",
                         "status",
                        ]
    
        # Ordenação padrão da listagem.
        ordering = ["cliente"]

@admin.register(ItemPedido)
class ItemPedidoAdmin (admin.ModelAdmin):
        
        # Colunas exibidas na listagem.
        list_display = ["id", 
                        "pedido",
                        "produto",
                        "quantidade",
                    ]
    
        # Campos pesquisáveis na caixa de busca.
        search_fields = ["produto", 
                         "preco_unitario",
                         "quantidade",
                         "pedido",
                        ]
    
        # Ordenação padrão da listagem.
        ordering = ["produto", "pedido"]

@admin.register(ComentarioAvaliacao)
class ComentarioAvaliacaoAdmin (admin.ModelAdmin):
        
        # Colunas exibidas na listagem.
        list_display = ["id", 
                        "cliente",
                        "nota",
                        "criado_em",
                    ]
    
        # Campos pesquisáveis na caixa de busca.
        search_fields = ["cliente", 
                         "produto",
                         "texto",
                         "nota",
                         "criado_em",
                        ]
    
        # Ordenação padrão da listagem.
        ordering = ["produto", "cliente"]
