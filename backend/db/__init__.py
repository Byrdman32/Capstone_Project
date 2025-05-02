import psycopg2
from psycopg2 import pool
from flask import g
from backend.constants import DB_CONFIG

db_pool = None

def init_db_pool(app):
    global db_pool
    db_pool = pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        user=DB_CONFIG['DB_USER'],
        password=DB_CONFIG['DB_PASSWORD'],
        host=DB_CONFIG['DB_HOST'],
        port=DB_CONFIG['DB_PORT'],
        database=DB_CONFIG['DB_NAME']
    )

def get_db():
    if 'db_conn' not in g:
        g.db_conn = db_pool.getconn()
    return g.db_conn

def close_db(e=None):
    conn = g.pop('db_conn', None)
    if conn:
        db_pool.putconn(conn)