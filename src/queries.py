import pandas as pd
from src.db import connect

engine = connect()

def get_table_names():
    query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';"
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

def get_table_data(table_name, limit=100):
    if not table_name.isidentifier():
        raise ValueError("Nom de table invalide")

    query = f"SELECT TOP {int(limit)} * FROM [{table_name}]"
    
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df


def get_full_schema():
    query = """
    SELECT 
        TABLE_NAME,
        COLUMN_NAME,
        DATA_TYPE,
        IS_NULLABLE,
        CHARACTER_MAXIMUM_LENGTH
    FROM INFORMATION_SCHEMA.COLUMNS
    ORDER BY TABLE_NAME, ORDINAL_POSITION
    """
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df
