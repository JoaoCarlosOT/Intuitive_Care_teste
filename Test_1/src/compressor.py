import os
import zipfile

# Definir a pasta onde os PDFs estão e onde o ZIP será salvo
PDF_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pdf_files"))
ZIP_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))
os.makedirs(ZIP_FOLDER, exist_ok=True)

def zip_files():
    # Compacta todos os PDFs da pasta pdf_files/ em um arquivo ZIP na pasta output/.
    zip_path = os.path.join(ZIP_FOLDER, "anexos.zip")
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_name in os.listdir(PDF_FOLDER):
            if file_name.endswith('.pdf'):
                file_path = os.path.join(PDF_FOLDER, file_name)
                zipf.write(file_path, os.path.basename(file_path))
    
    print(f"Arquivos compactados em {zip_path}")
