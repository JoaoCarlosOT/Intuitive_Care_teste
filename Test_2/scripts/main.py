import os
from extracao import extrair_tabela_pdf
from processamento import substituir_abreviacoes
from exportacao import salvar_e_zipar

# Caminho do PDF
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
PDF_PATH = os.path.join(BASE_DIR, "rol_procedimentos.pdf")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

NOME_ARQUIVO = "João_Carlos"

def main():
    df_dados = extrair_tabela_pdf(PDF_PATH)
    df_tratado = substituir_abreviacoes(df_dados)
    salvar_e_zipar(df_tratado, OUTPUT_DIR, NOME_ARQUIVO)

if __name__ == "__main__":
    main()
