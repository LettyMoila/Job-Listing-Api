import os
from psycopg2 import pool

conn_pool = pool.SimpleConnectionPool(
    1, 40,
    database = os.getenv('DB_NAME'),
    host = os.getenv('DB_HOST'),
    port = os.getenv('DB_PORT'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD')
)

class db_connect:
    def __init__(self, table):
        self.table = table
        self.pool = conn_pool
        
    def select(self, columns='*', condition=None, joins=None):
        connection = self.pool.getconn()
        cursor = connection.cursor()
        
        joins_stat = None

        if joins:
            for j in joins:
                tmp_st = f'FULL OUTER JOIN {j["table"]} ON {j["on_cond"]}'
                joins_stat = f'{str(joins_stat or "")} {tmp_st} '

        cursor.execute(f'SELECT {columns} FROM {self.table} {str(joins_stat or "")} {str(condition or "")}')

        rows = cursor.fetchall()

        connection.close()

        return rows

    def insert(self, columns, values):
        connection = self.pool.getconn()
        cursor = connection.cursor()

        sql = f"INSERT INTO {self.table} ({columns}) VALUES ({values}) RETURNING id;"

        cursor.execute(sql)
        
        curr_id = cursor.fetchone()[0]

        connection.commit()

        cursor.close()
        connection.close()

        return curr_id