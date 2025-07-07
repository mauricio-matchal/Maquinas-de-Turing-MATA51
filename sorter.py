# ESTE FOI O ARQUIVO PYTHON USADO PARA ORDENAR A PLANILHA DE TRANSIÇÕES DA MT1 E MT2
import pandas as pd
import re

arquivo_excel = "nome do arquivo desordenado.xlsx"

def extrair_numero(texto):
    match = re.search(r'\d+', str(texto))
    return int(match.group()) if match else 0

df = pd.read_excel(arquivo_excel)

nome_coluna_estado = df.columns[0]

df["ordem_temp"] = df[nome_coluna_estado].apply(extrair_numero)

df_ordenado = df.sort_values(by="ordem_temp").drop(columns=["ordem_temp"])

df_ordenado.to_excel("nome do arquivo ordenado.xlsx", index=False)

print(df_ordenado)
