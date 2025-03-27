from scraper import get_pdf_links
from downloader import download_pdfs
from compressor import zip_files

def main():
    print("Obtendo links dos PDFs...")
    pdf_links = get_pdf_links()
    
    if not pdf_links:
        print("Nenhum PDF encontrado.")
        return
    
    print("Baixando arquivos PDF...")
    download_pdfs(pdf_links)
    
    print("Compactando os arquivos baixados...")
    zip_files()
    
    print("Processo concluído!")

if __name__ == "__main__":
    main()
