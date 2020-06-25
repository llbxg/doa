import os

import psycopg2

table_name = 'blog'
dsn = os.environ.get('DATABASE_URL')

def get_connection():
    return psycopg2.connect(dsn)

def check_():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM %s'%table_name)
                return cur.fetchall()
    except:
        return [(0, '<p>error</P>', "Thu, 25 Jun 2020 00:00:00 GMT")]