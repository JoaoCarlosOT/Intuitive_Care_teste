import pdfplumber
import pandas as pd

def extrair_tabela_pdf(pdf_path):
    """
    Extrai os dados da tabela do PDF e retorna um DataFrame do pandas.
    """
    dados_tabela = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            tabela = pagina.extract_table()  # Extrai a tabela corretamente
            
            if tabela:
                dados_tabela.extend(tabela)  # Adiciona os dados extraídos

    # Converter a lista de listas em um DataFrame
    df = pd.DataFrame(dados_tabela)
    
    # Definir a primeira linha como cabeçalho
    df.columns = df.iloc[0]  # Primeira linha vira o nome das colunas
    df = df[1:]  # Remove a primeira linha, pois já virou cabeçalho
    
    return df
