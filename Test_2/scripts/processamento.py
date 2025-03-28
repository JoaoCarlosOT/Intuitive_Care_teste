import pandas as pd
import re

def processar_dados(texto):
    # Transforma o texto extraído do PDF em um DataFrame estruturado.
    linhas = texto.split("\n")
    dados = []

    for linha in linhas:
        colunas = re.split(r'\s{2,}', linha)  # Divide colunas por múltiplos espaços
        if len(colunas) >= 3:  # Ajuste conforme o formato do PDF
            dados.append(colunas)

    return pd.DataFrame(dados, columns=["Código", "Descrição", "OD", "AMB"])

def substituir_abreviacoes(df):
    # Substitui as abreviações OD e AMB por suas descrições completas.
    legenda = {"OD": "Odontológico", "AMB": "Ambulatorial"}
    df["OD"] = df["OD"].replace(legenda)
    df["AMB"] = df["AMB"].replace(legenda)
    return df
