# Banco de dados

## Tabela: categoria

Campos
- nome
    - charfield (15)
- descrição
    - charfield (50)

## Tabela: Produto
Campos
- nome  
    - charfield (15)
- descrição
    - charfield (15)
- preço
    - PositiveDecimalField(max_digits=10, decimal_places=2)
- quantidade
    - PositiveIntegerField(default=True)
- categoria (1 p/M)
    - ForeignKey

## Tabela: clientes
Campos:
- nome
    - charfield (50)
- nome_social
    - charfield (50)
- foto
    - ImageField
- tel
    - charfield (11) unique
- end
    - charfield (50)
- cpf (unico)
    - charfield (11) unique
- dt_nasc
    - DateField
- sexo
    - text.choices
- user (1 p/ 1)
    - onetoonefield

## Tabela: Pedido
- cliente (1 p/ muitos)
    - ForeignKey
- endereço (1 p/ muitos)
    - ForeignKey
- status
    - charfield (15)

## Tabela: Item pedido
- pedido (1 p/ muitos)
    - ForeignKey
- quantidade / preço
    - 


class Categoria(models.Model):
    """Representa uma categoria."""

    nome = models.CharField(max_length=15)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Produto (models.Model):
    nome = models.CharField(
        max_length=50,
    )
    descricao = models.CharField (
        max_length=100,
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    quantidade = models.PositiveIntegerField (
        default=1,
    )
    categoria = models.ForeignKey (
        Categoria,
        on_delete=models.CASCADE,
        related_name="produtos",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]
