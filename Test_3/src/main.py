import os
from models import criar_tabelas
from importer import importar_csv_operadoras, importar_csv_despesas
from queries import top_10_despesas, top_10_despesas_ano

def importar_arquivos_csv():
    base_dir = os.getcwd()  # Diretório base do projeto
    parent_dir = os.path.dirname(base_dir)  
    
    operadoras_dir = os.path.join(parent_dir, "uploads", "operadoras")
    despesas_dir = os.path.join(parent_dir, "uploads", "demonstracoes_contabeis")

    # Verificar se os diretórios existem
    if not os.path.exists(operadoras_dir):
        print(f"O diretório {operadoras_dir} não foi encontrado.")
        return
    if not os.path.exists(despesas_dir):
        print(f"O diretório {despesas_dir} não foi encontrado.")
        return

    # Importando operadoras
    for file in os.listdir(operadoras_dir):
        if file.endswith(".csv"):
            file_path = os.path.join(operadoras_dir, file)
            importar_csv_operadoras(file_path)

    
    for file in os.listdir(despesas_dir):
        if file.endswith(".csv"):
            file_path = os.path.join(despesas_dir, file)
            print(f"Importando despesas de {file}")
            importar_csv_despesas(file_path, trimestre="Desconhecido", ano=0)

if __name__ == "__main__":
    criar_tabelas()
    importar_arquivos_csv()
    top_10_despesas()  
    top_10_despesas_ano(2024)  
