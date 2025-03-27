import requests
from bs4 import BeautifulSoup
import os
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Pasta para salvar os PDFs
folder_name = "pdf_files"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Função para fazer download de um arquivo
def download_file(url, folder_name, file_name):
    response = requests.get(url)
    file_path = os.path.join(folder_name, file_name)
    
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Arquivo {file_name} baixado com sucesso!")

# Função para compactar os arquivos PDF em um arquivo ZIP
def zip_files(folder_name, zip_name):
    zip_path = os.path.join(folder_name, zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_name in os.listdir(folder_name):
            if file_name.endswith('.pdf'):
                file_path = os.path.join(folder_name, file_name)
                zipf.write(file_path, os.path.basename(file_path))
    print(f"Arquivos compactados em {zip_path}")

# Requisição para acessar a página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todos os links para os anexos (PDFs)
pdf_links = []
for a_tag in soup.find_all('a', href=True):
    if a_tag['href'].endswith('.pdf'):
        pdf_links.append(a_tag['href'])

# Baixar os PDFs
for pdf_link in pdf_links:
    if not pdf_link.startswith('http'):
        pdf_link = "https://www.gov.br" + pdf_link  # Corrigir o link relativo para absoluto
    file_name = pdf_link.split('/')[-1]  # Pega o nome do arquivo
    download_file(pdf_link, folder_name, file_name)

# Compactar os arquivos PDF
zip_files(folder_name, 'anexos.zip')
