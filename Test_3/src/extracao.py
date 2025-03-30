import os
import re
from models import criar_tabelas
from importer import importar_csv_operadoras, importar_csv_despesas
from queries import top_10_despesas, top_10_despesas_ano

def importar_arquivos_csv():
    # Definir diretórios de upload a partir do diretório atual
    operadoras_dir = os.path.join(os.getcwd(), "uploads", "operadoras")
    despesas_dir = os.path.join(os.getcwd(), "uploads", "demonstracoes_contabeis")

    # Verificar se os diretórios existem antes de tentar listar arquivos
    if not os.path.exists(operadoras_dir):
        print(f"O diretório {operadoras_dir} não foi encontrado.")
        return
    if not os.path.exists(despesas_dir):
        print(f"O diretório {despesas_dir} não foi encontrado.")
        return

    # Importar todos os arquivos CSV de operadoras
    for file in os.listdir(operadoras_dir):
        if file.endswith(".csv"):
            file_path = os.path.join(operadoras_dir, file)
            importar_csv_operadoras(file_path)

    # Importar todos os arquivos CSV de despesas
    for file in os.listdir(despesas_dir):
        if file.endswith(".csv"):
            file_path = os.path.join(despesas_dir, file)
            
            # Extrair o trimestre e o ano do nome do arquivo, exemplo: '2T2024.csv'
            match = re.match(r'(\d)T(\d{4})\.csv', file)  # Exemplo: 2T2024.csv
            if match:
                trimestre = match.group(1)
                ano = match.group(2)
                print(f"Importando despesas para Trimestre: {trimestre}, Ano: {ano} de {file}")
                
                # Chamar a função de importação de despesas passando o trimestre e ano
                importar_csv_despesas(file_path, trimestre, ano)

if __name__ == "__main__":
    criar_tabelas()
    importar_arquivos_csv()
    top_10_despesas("4", 2024)  # Último trimestre
    top_10_despesas_ano(2024)   # Último ano
