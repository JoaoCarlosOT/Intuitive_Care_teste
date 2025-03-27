import requests
from bs4 import BeautifulSoup
import os
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Definir a pasta para salvar os PDFs (fora do diretório 'src/')
pdf_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pdf_files")

# Definir a pasta para salvar o ZIP (fora do diretório 'src/', na pasta 'output')
zip_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output")

# Criar as pastas se não existirem
os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(zip_folder, exist_ok=True)

# Função para fazer download de um arquivo
def download_file(url, folder_name, file_name):
    response = requests.get(url)
    file_path = os.path.join(folder_name, file_name)
    
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Arquivo {file_name} baixado com sucesso!")

# Função para compactar os arquivos PDF na pasta 'output'
def zip_files(pdf_folder, zip_folder, zip_name):
    zip_path = os.path.join(zip_folder, zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_name in os.listdir(pdf_folder):
            if file_name.endswith('.pdf'):
                file_path = os.path.join(pdf_folder, file_name)
                zipf.write(file_path, os.path.basename(file_path))
    print(f"Arquivos compactados em {zip_path}")

# Requisição para acessar a página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todos os links para os anexos (PDFs)
pdf_links = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    text = a_tag.get_text(strip=True)  # Pega o texto do link

    # Filtrar links que contêm "Anexo I" ou "Anexo II"
    if href.endswith('.pdf') and ("Anexo I" in text or "Anexo II" in text):
        pdf_links.append(href)

# Baixar os PDFs filtrados
for pdf_link in pdf_links:
    if not pdf_link.startswith('http'):
        pdf_link = "https://www.gov.br" + pdf_link  # Corrigir o link relativo para absoluto
    file_name = pdf_link.split('/')[-1]  # Pega o nome do arquivo
    download_file(pdf_link, pdf_folder, file_name)

# Compactar os arquivos PDF e salvar na pasta 'output'
zip_files(pdf_folder, zip_folder, 'anexos.zip')
