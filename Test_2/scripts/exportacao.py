import os
import zipfile

OUTPUT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "output"))
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  

def salvar_e_zipar(df, output_dir, nome_arquivo):
    
    csv_filename = os.path.join(output_dir, f"Teste_{nome_arquivo}.csv")
    zip_filename = os.path.join(output_dir, f"Teste_{nome_arquivo}.zip")

    df.to_csv(csv_filename, index=False)
    
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(csv_filename, os.path.basename(csv_filename))  

    print(f"Arquivo ZIP criado com sucesso: {zip_filename}")
