import os

import psycopg2
from psycopg2.extras import DictCursor

table_blog = 'blog'
table_ff = 'ff'
dsn = os.environ.get('DATABASE_URL')

def get_connection():
    return psycopg2.connect(dsn)

def reg_f(cur, _id, inbox):
    sql = "INSERT INTO {} (id, inbox) VALUES (%s, %s)".format(table_ff)
    data = (_id, inbox)
    cur.execute(sql, data)

def del_f(cur, _id):
    sql = "DELETE FROM {} WHERE id = %s;".format(table_ff)
    data = (_id,)
    cur.execute(sql, data)

def check_all(table=table_blog):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM %s'%table)
                return cur.fetchall()
    except:
        return [(0, '<p>error</P>', "Thu, 25 Jun 2020 00:00:00 GMT")]

def get_article(_id):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            sql = "SELECT * FROM {} where id = %s".format('blog')
            cur.execute(sql,(_id,))
            return dict(cur.fetchone())

def check_followers(_id, inbox):
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM {} where id = %s".format(table_ff)
            cur.execute(sql,(_id,))
            if cur.fetchone() is None:
                reg_f(cur, _id, inbox)

def del_followers(_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM {} where id = %s".format(table_ff)
            cur.execute(sql,(_id,))
            if cur.fetchone() is not None:
                del_f(cur, _id)