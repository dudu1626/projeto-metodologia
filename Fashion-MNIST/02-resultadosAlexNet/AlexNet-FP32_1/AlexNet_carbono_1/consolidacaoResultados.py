# Script de consolidação dos dados dos arquivos CSV em um único arquivo.

import pandas as pd
import os


#obter o diretório atual
diretorio = os.getcwd()

# Nome base dos arquivos
nome_base = "emissoes_treino_modelo_"

# Lista para armazenar os DataFrames
lista_dfs = []

# Ler todos os 10 arquivos
for i in range(1, 11):
    nome_arquivo = f"{nome_base}{i}.csv"
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    try:
        df = pd.read_csv(caminho_arquivo)
        df["arquivo_origem"] = nome_arquivo  # Adiciona coluna para identificar a origem
        lista_dfs.append(df)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {nome_arquivo}")

# Concatenar todos os DataFrames
df_consolidado = pd.concat(lista_dfs, ignore_index=True)

# Exportar para Excel
caminho_saida = os.path.join(diretorio, "consolidado_emissoes_treino.xlsx")
df_consolidado.to_excel(caminho_saida, index=False)

print(f"Arquivo consolidado salvo em: {caminho_saida}")


# Nome base dos arquivos
nome_base = "emissoes_teste_"

# Lista para armazenar os DataFrames
lista_dfs = []

# Ler todos os 10 arquivos
for i in range(1, 11):
    nome_arquivo = f"{nome_base}{i}.csv"
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    try:
        df = pd.read_csv(caminho_arquivo)
        df["arquivo_origem"] = nome_arquivo  # Adiciona coluna para identificar a origem
        lista_dfs.append(df)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {nome_arquivo}")

# Concatenar todos os DataFrames
df_consolidado = pd.concat(lista_dfs, ignore_index=True)

# Exportar para Excel
caminho_saida = os.path.join(diretorio, "consolidado_emissoes_teste.xlsx")
df_consolidado.to_excel(caminho_saida, index=False)

print(f"Arquivo consolidado salvo em: {caminho_saida}")
