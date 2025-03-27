import os
import requests

# Definir a pasta para salvar os PDFs (fora do diretório 'src/')
PDF_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pdf_files"))
os.makedirs(PDF_FOLDER, exist_ok=True)

def download_file(url):
    # Faz o download de um arquivo PDF e salva na pasta pdf_files/.
    file_name = url.split('/')[-1]
    file_path = os.path.join(PDF_FOLDER, file_name)

    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    print(f"Arquivo {file_name} baixado com sucesso!")

def download_pdfs(pdf_links):
    # Baixa todos os PDFs encontrados.
    for link in pdf_links:
        download_file(link)
