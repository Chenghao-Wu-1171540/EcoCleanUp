# loginapp/db.py
"""
PostgreSQL database helper for Flask app (using g + app context)
COMP639 EcoCleanUp Hub
"""

from flask import g, current_app
import psycopg2
from psycopg2.extras import RealDictCursor

def init_db(app):
    from loginapp.connect import dbuser, dbpass, dbhost, dbport, dbname

    app.config['DB_PARAMS'] = {
        'user': dbuser,
        'password': dbpass,
        'host': dbhost,
        'port': dbport,
        'dbname': dbname,
    }

    app.teardown_appcontext(close_db)


def get_db():
    """
    get connect (use g)
    """
    if 'db' not in g:
        params = current_app.config['DB_PARAMS']
        g.db = psycopg2.connect(**params, cursor_factory=RealDictCursor)
        # 可选：设置 autocommit（大多数 web app 建议 True）
        g.db.autocommit = True
    return g.db


def get_cursor():
    return get_db().cursor()


def close_db(exception=None):
    """
    auto close db
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def test_connection():
    from loginapp.connect import dbuser, dbpass, dbhost, dbport, dbname
    try:
        conn = psycopg2.connect(
            user=dbuser,
            password=dbpass,
            host=dbhost,
            port=dbport,
            dbname=dbname,
            cursor_factory=RealDictCursor
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        print("PostgreSQL 版本:", cur.fetchone()['version'])
        cur.close()
        conn.close()
        print("success")
    except Exception as e:
        print("error:", str(e))


if __name__ == '__main__':
    test_connection()