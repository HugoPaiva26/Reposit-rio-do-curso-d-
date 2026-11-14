
"""
Script para cadastrar produtos no banco de dados Django.

Projeto: config
Aplicação: apps.produtos
Model: Produto

Execução:
    python _scripts/cadastrar_produtos.py
"""

import os
import sys
import json

from pathlib import Path
from decimal import Decimal, InvalidOperation


# ==========================================================
# 1. CONFIGURAÇÃO DOS DIRETÓRIOS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DADOS_DIR = BASE_DIR / "_dados"

ARQUIVO_DADOS = DADOS_DIR / "produtos.json"


# ==========================================================
# 2. CONFIGURAÇÃO DO DJANGO
# ==========================================================

sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

import django

django.setup()


# ==========================================================
# 3. IMPORTAÇÃO DOS MODELS
# ==========================================================

from apps.produtos.models import Produto, Categoria


# ==========================================================
# 4. FUNÇÃO PARA CARREGAR OS DADOS
# ==========================================================

def carregar_dados():
    """
    Carrega os produtos do arquivo JSON.
    """

    if not ARQUIVO_DADOS.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {ARQUIVO_DADOS}"
        )

    with open(
        ARQUIVO_DADOS,
        "r",
        encoding="utf-8"
    ) as arquivo:

        dados = json.load(arquivo)

    if not isinstance(dados, list):
        raise ValueError(
            "O arquivo JSON deve conter uma lista de produtos."
        )

    return dados


# ==========================================================
# 5. FUNÇÃO PARA VALIDAR OS DADOS
# ==========================================================

def validar_produto(item):
    """
    Valida os dados básicos de um produto.
    """

    nome = item.get("nome", "").strip()

    categoria = item.get("categoria", "").strip()

    descricao = item.get("descricao", "")

    preco = item.get("preco")

    quantidade_estoque = item.get("quantidade_estoque", 0)

    if not nome:
        raise ValueError("Nome do produto não informado.")

    if len(nome) > 150:
        raise ValueError(
            f"Nome do produto excede 150 caracteres: {nome}"
        )

    if not categoria:
        raise ValueError(
            f"Categoria não informada para o produto: {nome}"
        )

    if preco is None:
        raise ValueError(
            f"Preço não informado para o produto: {nome}"
        )

    try:
        preco = Decimal(str(preco))

    except InvalidOperation:
        raise ValueError(
            f"Preço inválido para o produto: {nome}"
        )

    if not preco.is_finite() or preco < 0:
        raise ValueError(
            f"Preço inválido para o produto: {nome}"
        )

    if preco.as_tuple().exponent < -2:
        raise ValueError(
            f"Preço deve possuir no máximo duas casas decimais: {nome}"
        )

    if preco > Decimal("99999999.99"):
        raise ValueError(
            f"Preço excede o limite permitido: {nome}"
        )

    if (
        isinstance(quantidade_estoque, bool)
        or not isinstance(quantidade_estoque, int)
        or quantidade_estoque < 0
    ):
        raise ValueError(
            f"Estoque inválido para o produto: {nome}"
        )

    return {
        "nome": nome,
        "categoria": categoria,
        "descricao": descricao or "",
        "preco": preco,
        "quantidade_estoque": quantidade_estoque,
    }


# ==========================================================
# 6. FUNÇÃO PARA CADASTRAR OS PRODUTOS
# ==========================================================

def cadastrar_produtos():

    produtos = carregar_dados()

    cadastrados = 0
    existentes = 0
    ignorados = 0

    print("\nIniciando cadastro de produtos...")
    print("-" * 60)

    for item in produtos:

        try:

            # Valida os dados do produto.
            dados = validar_produto(item)

            nome = dados["nome"]

            nome_categoria = dados["categoria"]

            # Localiza a categoria no banco de dados.
            try:

                categoria = Categoria.objects.get(
                    nome=nome_categoria
                )

            except Categoria.DoesNotExist:

                ignorados += 1

                print(
                    f"[IGNORADO] Categoria não encontrada: "
                    f"{nome_categoria} ({nome})"
                )

                continue

            # Cadastra o produto caso ainda não exista.
            produto, criado = Produto.objects.get_or_create(
                nome=nome,
                defaults={
                    "categoria": categoria,
                    "descricao": dados["descricao"],
                    "preco": dados["preco"],
                    "quantidade_estoque": dados["quantidade_estoque"],
                }
            )

            if criado:

                cadastrados += 1

                print(
                    f"[OK] Produto cadastrado: {produto.nome}"
                )

            else:

                existentes += 1

                print(
                    f"[EXISTENTE] Produto: {produto.nome}"
                )

        except (ValueError, TypeError) as erro:

            ignorados += 1

            print(
                f"[ERRO] {erro}"
            )

    # ======================================================
    # 7. RESUMO DA EXECUÇÃO
    # ======================================================

    print("\n" + "=" * 60)
    print("RESUMO DO CADASTRO DE PRODUTOS")
    print("=" * 60)

    print(f"Total de produtos no arquivo: {len(produtos)}")

    print(f"Novos produtos cadastrados:   {cadastrados}")

    print(f"Produtos já existentes:      {existentes}")

    print(f"Produtos ignorados:          {ignorados}")

    print(f"Total no banco de dados:     {Produto.objects.count()}")

    print("=" * 60)

    print("Processamento finalizado!\n")


# ==========================================================
# 8. EXECUÇÃO PRINCIPAL
# ==========================================================

if __name__ == "__main__":

    try:

        cadastrar_produtos()

    except Exception as erro:

        print(f"\nERRO AO EXECUTAR O SCRIPT: {erro}")

        sys.exit(1)
