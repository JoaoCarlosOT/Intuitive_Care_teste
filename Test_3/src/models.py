from database import Database

def criar_tabelas():
    db = Database()
    query = """
    CREATE TABLE IF NOT EXISTS operadoras (
        id SERIAL PRIMARY KEY,
        registro_ans VARCHAR(50) UNIQUE,
        razao_social VARCHAR(255),
        cnpj VARCHAR(50)
    );

    CREATE TABLE IF NOT EXISTS despesas (
        id SERIAL PRIMARY KEY,
        registro_ans VARCHAR(50),
        trimestre VARCHAR(10),
        ano INT,
        despesas_medico_hospitalar DECIMAL(15,2),
        FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
    );
    """
    db.execute_query(query)
    print("Tabelas criadas com sucesso!")
