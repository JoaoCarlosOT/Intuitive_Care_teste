import os
from models import criar_tabelas
from importer import importar_csv_operadoras, importar_csv_despesas
from queries import top_10_despesas, top_10_despesas_ano

def importar_arquivos_csv():
    base_dir = os.getcwd()  # Diretório base do projeto
    operadoras_dir = os.path.join(base_dir, "uploads", "operadoras")
    despesas_dir = os.path.join(base_dir, "uploads", "demonstracoes_contabeis")

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

    # Importando despesas sem considerar o nome do arquivo
    for file in os.listdir(despesas_dir):
        if file.endswith(".csv"):
            file_path = os.path.join(despesas_dir, file)
            print(f"Importando despesas de {file}")
            importar_csv_despesas(file_path, trimestre="Desconhecido", ano=0)  # Removemos a dependência do nome do arquivo

if __name__ == "__main__":
    criar_tabelas()
    importar_arquivos_csv()
    top_10_despesas("4", 2024)  # Último trimestre
    top_10_despesas_ano(2024)   # Último ano
