from database import Database

db = Database()

def top_10_despesas(trimestre, ano):
    query = f"""
    SELECT o.razao_social, SUM(d.despesas_medico_hospitalar) as total_despesas
    FROM despesas d
    JOIN operadoras o ON d.registro_ans = o.registro_ans
    WHERE d.ano = {ano} AND d.trimestre = '{trimestre}'
    GROUP BY o.razao_social
    ORDER BY total_despesas DESC
    LIMIT 10;
    """
    df = db.fetch_dataframe(query)
    print(df)

def top_10_despesas_ano(ano):
    query = f"""
    SELECT o.razao_social, SUM(d.despesas_medico_hospitalar) as total_despesas
    FROM despesas d
    JOIN operadoras o ON d.registro_ans = o.registro_ans
    WHERE d.ano = {ano}
    GROUP BY o.razao_social
    ORDER BY total_despesas DESC
    LIMIT 10;
    """
    df = db.fetch_dataframe(query)
    print(df)
