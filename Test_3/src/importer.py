import pandas as pd
from database import Database

db = Database()

def importar_csv_operadoras(csv_path):
    print(f"Importando operadoras de {csv_path}...")

    try:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8", dtype=str)

        df.rename(columns={
            "Registro_ANS": "registro_ans",
            "CNPJ": "cnpj",
            "Razao_Social": "razao_social",
            "Nome_Fantasia": "nome_fantasia",
            "Modalidade": "modalidade",
            "Logradouro": "logradouro",
            "Numero": "numero",
            "Complemento": "complemento",
            "Bairro": "bairro",
            "Cidade": "cidade",
            "UF": "uf",
            "CEP": "cep",
            "DDD": "ddd",
            "Telefone": "telefone",
            "Fax": "fax",
            "Endereco_eletronico": "endereco_eletronico",
            "Representante": "representante",
            "Cargo_Representante": "cargo_representante",
            "Regiao_de_Comercializacao": "regiao_de_comercializacao",
            "Data_Registro_ANS": "data_registro_ans"
        }, inplace=True)

        df["data_registro_ans"] = pd.to_datetime(df["data_registro_ans"], errors="coerce")

        # Inserindo no banco de dados
        df.to_sql("operadoras", db.engine, if_exists="append", index=False)
        print("Operadoras importadas com sucesso!")

    except Exception as e:
        print(f"Erro ao importar operadoras de {csv_path}: {e}")

def importar_csv_despesas(csv_path, trimestre, ano):
    print(f"Importando despesas de {csv_path} para o trimestre {trimestre}, ano {ano}...")

    try:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8", dtype=str)

        df.rename(columns={
            "DATA": "data",
            "REG_ANS": "reg_ans",
            "CD_CONTA_CONTABIL": "cd_conta_contabil",
            "DESCRICAO": "descricao",
            "VL_SALDO_INICIAL": "vl_saldo_inicial",
            "VL_SALDO_FINAL": "vl_saldo_final"
        }, inplace=True)

        df["data"] = pd.to_datetime(df["data"], errors="coerce")
        df["vl_saldo_inicial"] = pd.to_numeric(df["vl_saldo_inicial"], errors="coerce").fillna(0)
        df["vl_saldo_final"] = pd.to_numeric(df["vl_saldo_final"], errors="coerce").fillna(0)

        df["trimestre"] = trimestre
        df["ano"] = ano

        # Inserindo no banco de dados
        df.to_sql("despesas", db.engine, if_exists="append", index=False)
        print("Despesas importadas com sucesso!")

    except Exception as e:
        print(f"Erro ao importar despesas de {csv_path}: {e}")
