import pandas as pd
from database import Database

db = Database()

def importar_csv_operadoras(csv_path):
    df = pd.read_csv(csv_path, sep=';', encoding='latin1')
    df = df.rename(columns={'Registro ANS': 'registro_ans', 'Razão Social': 'razao_social', 'CNPJ': 'cnpj'})
    df[['registro_ans', 'razao_social', 'cnpj']].to_sql('operadoras', db.engine, if_exists='append', index=False)
    print("Operadoras importadas com sucesso!")

def importar_csv_despesas(csv_path):
    df = pd.read_csv(csv_path, sep=';', encoding='latin1')
    df = df.rename(columns={'Registro ANS': 'registro_ans', 'Ano': 'ano', 'Trimestre': 'trimestre',
                             'Eventos/Sinistros Conhecidos ou Avisados de Assistência à Saúde Médico Hospitalar': 'despesas_medico_hospitalar'})
    df[['registro_ans', 'ano', 'trimestre', 'despesas_medico_hospitalar']].to_sql('despesas', db.engine, if_exists='append', index=False)
    print("Despesas importadas com sucesso!")
