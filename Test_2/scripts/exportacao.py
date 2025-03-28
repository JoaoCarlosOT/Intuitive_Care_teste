import os
import zipfile

# Definir a pasta onde os CSVs serão salvos e o ZIP será armazenado
OUTPUT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "output"))
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Cria a pasta se não existir

def salvar_e_zipar(df, output_dir, nome_arquivo):
    # Salva o DataFrame em CSV e compacta em um arquivo ZIP na pasta correta.
    
    csv_filename = os.path.join(output_dir, f"Teste_{nome_arquivo}.csv")
    zip_filename = os.path.join(output_dir, f"Teste_{nome_arquivo}.zip")

    # Salvar o CSV
    df.to_csv(csv_filename, index=False)
    
    # Compactar o CSV em um ZIP
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(csv_filename, os.path.basename(csv_filename))  # Garante que o nome do arquivo no ZIP está correto

    print(f"Arquivo ZIP criado com sucesso: {zip_filename}")
