
"""
Script para cadastrar categorias no banco de dados Django.

Projeto: config
Aplicação: apps.produtos
Model: Categoria

Execução:
    python _scripts/cadastrar_categorias.py
"""

import os
import sys
import json

from pathlib import Path


# ==========================================================
# 1. CONFIGURAÇÃO DOS DIRETÓRIOS
# ==========================================================

# Diretório raiz do projeto Django.
BASE_DIR = Path(__file__).resolve().parent.parent

# Diretório contendo os arquivos de dados.
DADOS_DIR = BASE_DIR / "_dados"

# Arquivo JSON com as categorias.
ARQUIVO_DADOS = DADOS_DIR / "categorias.json"


# ==========================================================
# 2. CONFIGURAÇÃO DO DJANGO
# ==========================================================

# Adiciona a raiz do projeto ao caminho de importação Python.
sys.path.insert(0, str(BASE_DIR))

# Define o módulo de configurações do Django.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

# Inicializa o Django.
import django

django.setup()


# ==========================================================
# 3. IMPORTAÇÃO DO MODEL
# ==========================================================

from apps.produtos.models import Categoria


# ==========================================================
# 4. FUNÇÃO PARA CARREGAR OS DADOS
# ==========================================================

def carregar_dados():
    """
    Carrega as categorias do arquivo JSON.
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
            "O arquivo JSON deve conter uma lista de categorias."
        )

    return dados


# ==========================================================
# 5. FUNÇÃO PARA CADASTRAR AS CATEGORIAS
# ==========================================================

def cadastrar_categorias():
    """
    Cadastra as categorias utilizando o ORM do Django.
    """

    categorias = carregar_dados()

    cadastradas = 0
    existentes = 0

    print("\nIniciando cadastro de categorias...")
    print("-" * 50)

    for item in categorias:

        nome = item.get("nome", "").strip()
        descricao = item.get("descricao", "")

        # Validação do nome.
        if not nome:
            print("Categoria ignorada: nome não informado.")
            continue

        # Impede nomes maiores que o limite do model.
        if len(nome) > 100:
            print(f"Categoria ignorada: {nome[:50]} (nome muito longo).")
            continue

        # Cria a categoria somente se ela ainda não existir.
        categoria, criada = Categoria.objects.get_or_create(
            nome=nome,
            defaults={
                "descricao": descricao
            }
        )

        if criada:
            cadastradas += 1
            print(f"[OK] Categoria cadastrada: {categoria.nome}")

        else:
            existentes += 1
            print(f"[EXISTENTE] Categoria: {categoria.nome}")

    # ======================================================
    # 6. RESUMO DA EXECUÇÃO
    # ======================================================

    print("\n" + "=" * 50)
    print("RESUMO DO CADASTRO")
    print("=" * 50)

    print(f"Total de categorias no arquivo: {len(categorias)}")
    print(f"Novas categorias cadastradas:   {cadastradas}")
    print(f"Categorias já existentes:      {existentes}")
    print(f"Total no banco de dados:        {Categoria.objects.count()}")

    print("=" * 50)
    print("Processamento finalizado!\n")


# ==========================================================
# 7. EXECUÇÃO PRINCIPAL
# ==========================================================

if __name__ == "__main__":

    try:
        cadastrar_categorias()

    except Exception as erro:
        print(f"\nERRO AO EXECUTAR O SCRIPT: {erro}")
        sys.exit(1)
