import os
import pandas as pd

# Função para carregar todos os dados do CSV e converter para JSON
def load_data():
    try:
        # Construindo o caminho do arquivo CSV usando a biblioteca os
        file_path = os.path.join('uploads', 'operadoras.csv')
        print(f"Procurando arquivo em: {file_path}")  # Debug: Verificar caminho

        # Verificar se o arquivo existe
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
        
        # Lendo o arquivo CSV da pasta 'uploads' com delimitador ponto e vírgula
        df = pd.read_csv(file_path, delimiter=';')
        print(f"Dados lidos com sucesso: {df.head()}")  # Debug: Verificar dados lidos
        
        # Adiciona o campo 'id' com auto-increment
        df['id'] = range(1, len(df) + 1)  # Cria a coluna 'id' com valores de 1 até o número total de registros

        # Converte o DataFrame para uma lista de dicionários
        return df.to_dict(orient='records')

    except Exception as e:
        print(f"Erro ao carregar o CSV: {e}")  # Mensagem de erro detalhada
        return None
