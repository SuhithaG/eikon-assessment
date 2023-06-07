import psycopg2
import pandas as pd
from sqlalchemy import create_engine


# function to write data into postgres table
def insert_into_table(df, table_name):
    engine = create_engine('postgresql://test_db:docker@database:5432/docker')
    df.to_sql(table_name, engine, if_exists='replace')


# A utility postgres class to perform needed operations
class PostgresUtils:
    def __init__(self, db, user, pwd):
        self.db = db,
        self.user = user,
        self.pwd = pwd,
        self.conn = psycopg2.connect(
            host="database",
            database=self.db,
            user=self.user,
            password=self.pwd)

        self.results = None

    # Get the cursor
    def get_cursor(self):
        return self.conn.cursor()

    def create_database(self, db_name):
        cur = self.get_cursor()
        sql = "CREATE DATABASE {db_name}".format(db_name=db_name)
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def create_table(self, table_name):
        cur = self.get_cursor()
        sql = """ CREATE TABLE IF NOT EXISTS {table} ( 
            user_id INTEGER PRIMARY KEY,
            total_experiments INTEGER,
            avg_runtime FLOAT,
            most_common_compound_id STRING)""".format(table=table_name)

        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def fetch_table_rows(self, table_name):
        sql = "SELECT * FROM {table}".format(table=table_name)
        self.results = pd.read_sql(sql, con=self.conn)
        return self.results

    def download_results(self):
        self.results.to_csv('results.csv', sep=",", index=False)
