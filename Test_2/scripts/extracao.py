import pdfplumber
import pandas as pd

def extrair_tabela_pdf(pdf_path):
    
    dados_tabela = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            tabela = pagina.extract_table() 
            
            if tabela:
                dados_tabela.extend(tabela)  

    df = pd.DataFrame(dados_tabela)
    
    df.columns = df.iloc[0]  
    df = df[1:]  
    
    return df
