from sqlalchemy import create_engine, text  
from config import DB_TYPE, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

class Database:
    def __init__(self):
        self.engine = create_engine(f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    def execute_query(self, query):
        with self.engine.connect() as conn:
            conn.execute(text(query))  # Aqui, 'text(query)' transforma a string SQL em uma instrução executável
            conn.commit()  

    def fetch_dataframe(self, query):
        import pandas as pd
        return pd.read_sql(query, self.engine)
