import sqlite3
import pandas as pd

def save_to_sqlite(df : pd.DataFrame,db_name: str,table_name: str):
    with sqlite3.connect(db_name) as conn:     
        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )
    print(f"数据已写入SQLite{db_name}表名为{table_name}")




def query_posts(sql : str,dbname: str)-> pd.DataFrame:
    with sqlite3.connect(dbname) as conn:
        return pd.read_sql(sql,conn)
