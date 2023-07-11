import os
from psycopg2 import pool

connect = pool.SimpleConnectionPool(
    1, 40,
    database = os.getenv('DB_NAME'),
    host = os.getenv('DB_HOST'),
    port = os.getenv('DB_PORT'),
    username = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD')
    
)

class db_connect:
    def __init__(self, table):
        self.table = table
        self.pool = connect
        
    def select(self, columns='*', condition=None, joins=None):
        connection = self.pool.getconn()
        cursor = connection.cursor()
        
        joins_stat=None

        if joins:
            for j in joins:
                tmp_st = f'FULL OUTER JOIN {j["table"]} ON {j["on_cond"]}'
                joins_stat = f'{str(joins_stat or "")} {tmp_st} '

        cursor.execute(f'SELECT {columns} FROM {self.table} {str(joins_stat or "")} {str(condition or "")} ORDER BY {self.table}.id ASC')

        rows = cursor.fetchall()

        connection.close()

        return rows
