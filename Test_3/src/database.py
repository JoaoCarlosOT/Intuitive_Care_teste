from sqlalchemy import create_engine, text  # Importe o 'text' corretamente
from config import DB_TYPE, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

class Database:
    def __init__(self):
        self.engine = create_engine(f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    def execute_query(self, query):
        # Utilize text() para garantir que o SQL seja tratado corretamente
        with self.engine.connect() as conn:
            conn.execute(text(query))  # Aqui, 'text(query)' transforma a string SQL em uma instrução executável
            conn.commit()  # Para garantir que as alterações sejam aplicadas ao banco de dados

    def fetch_dataframe(self, query):
        import pandas as pd
        return pd.read_sql(query, self.engine)
