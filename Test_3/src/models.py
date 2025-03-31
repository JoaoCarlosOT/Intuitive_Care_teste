from database import Database

def criar_tabelas():
    db = Database()
    query = """
    CREATE TABLE IF NOT EXISTS operadoras (
        id SERIAL PRIMARY KEY,
        registro_ans VARCHAR(50) UNIQUE,
        cnpj VARCHAR(50),
        razao_social VARCHAR(255),
        nome_fantasia VARCHAR(255),
        modalidade VARCHAR(100),
        logradouro VARCHAR(255),
        numero VARCHAR(20),
        complemento VARCHAR(255),
        bairro VARCHAR(100),
        cidade VARCHAR(100),
        uf VARCHAR(2),
        cep VARCHAR(20),
        ddd VARCHAR(5),
        telefone VARCHAR(20),
        fax VARCHAR(20),
        endereco_eletronico VARCHAR(255),
        representante VARCHAR(255),
        cargo_representante VARCHAR(100),
        regiao_de_comercializacao VARCHAR(100),
        data_registro_ans DATE
    );

    CREATE TABLE IF NOT EXISTS despesas (
        id SERIAL PRIMARY KEY,
        data DATE,
        reg_ans VARCHAR(50),
        cd_conta_contabil VARCHAR(20),
        descricao VARCHAR(255),
        vl_saldo_inicial DECIMAL(15,2),
        vl_saldo_final DECIMAL(15,2),
        trimestre VARCHAR(10),
        ano INT,
        FOREIGN KEY (reg_ans) REFERENCES operadoras(registro_ans)
    );
    """
    db.execute_query(query)
    print("Tabelas criadas com sucesso!")
