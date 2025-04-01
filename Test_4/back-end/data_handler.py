import os
import pandas as pd

def load_data():
    try:
        file_path = os.path.join('uploads', 'operadoras.csv')
        print(f"Procurando arquivo em: {file_path}")  

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
        
        df = pd.read_csv(file_path, delimiter=';')
        print(f"Dados lidos com sucesso: {df.head()}") 
        
        df['id'] = range(1, len(df) + 1) 

        return df.to_dict(orient='records')

    except Exception as e:
        print(f"Erro ao carregar o CSV: {e}")  
        return None
