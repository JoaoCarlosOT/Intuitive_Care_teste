import requests
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def get_pdf_links():
    # Obtém os links dos PDFs que contêm 'Anexo I' e 'Anexo II'.
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    pdf_links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        text = a_tag.get_text(strip=True)

        if href.endswith('.pdf') and ("Anexo I" in text or "Anexo II" in text):
            if not href.startswith('http'):
                href = "https://www.gov.br" + href  # Corrigir link relativo para absoluto
            pdf_links.append(href)
    
    return pdf_links
