from database import Database

db = Database()

def top_10_despesas():
    query = """
    WITH UltimosTresMeses AS (
        SELECT MAX(ano) AS ultimo_ano, 
               MAX(CASE WHEN MONTH(data) BETWEEN 10 AND 12 THEN MONTH(data) END) AS ultimo_mes
        FROM despesas
        WHERE YEAR(data) = 2024
    )
    SELECT o.razao_social, SUM(d.vl_saldo_final) AS total_despesas
    FROM despesas d
    JOIN operadoras o ON d.reg_ans = o.registro_ans
    JOIN UltimosTresMeses ut ON d.ano = ut.ultimo_ano AND MONTH(d.data) = ut.ultimo_mes
    WHERE YEAR(d.data) = 2024
    GROUP BY o.razao_social
    ORDER BY total_despesas DESC
    LIMIT 10;
    """
    df = db.fetch_dataframe(query)
    print("As 10 operadoras com maiores despesas em EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR no último trimestre são:")
    print(df)

def top_10_despesas_ano(ano):
    query = f"""
    SELECT o.razao_social, SUM(d.vl_saldo_final) AS total_despesas
    FROM despesas d
    JOIN operadoras o ON d.reg_ans = o.registro_ans
    WHERE YEAR(d.data) = {ano}
    GROUP BY o.razao_social
    ORDER BY total_despesas DESC
    LIMIT 10;
    """
    df = db.fetch_dataframe(query)
    print(f"As 10 operadoras com maiores despesas nessa categoria no ano de {ano} são:")
    print(df)
