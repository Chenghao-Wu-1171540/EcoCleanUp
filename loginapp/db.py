# loginapp/db.py
"""
PostgreSQL database helper for Flask app using Flask's application context (g).
This is the recommended way for EcoCleanUp Hub (COMP639 S1 2026).
"""

from flask import g, current_app
import psycopg2
from psycopg2.extras import RealDictCursor

def init_db(app):
    """Called once when the Flask app starts. Loads connection details from connect.py."""
    from loginapp.connect import dbuser, dbpass, dbhost, dbport, dbname

    app.config['DB_PARAMS'] = {
        'user': dbuser,
        'password': dbpass,
        'host': dbhost,
        'port': dbport,
        'dbname': dbname,
    }

    # Automatically close DB connection at the end of every request
    app.teardown_appcontext(close_db)


def get_db():
    """Returns the same DB connection for the current request (stored in g)."""
    if 'db' not in g:
        params = current_app.config['DB_PARAMS']
        g.db = psycopg2.connect(**params, cursor_factory=RealDictCursor)
        g.db.autocommit = True   # Most web apps should use autocommit=True
    return g.db


def get_cursor():
    """Convenience function to get a new cursor."""
    return get_db().cursor()


def close_db(exception=None):
    """Automatically called by Flask at the end of each request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()


# Quick test: python loginapp/db.py
if __name__ == '__main__':
    from loginapp.connect import dbuser, dbpass, dbhost, dbport, dbname
    try:
        conn = psycopg2.connect(user=dbuser, password=dbpass, host=dbhost,
                                port=dbport, dbname=dbname,
                                cursor_factory=RealDictCursor)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        print("✅ PostgreSQL connected successfully")
        print("Version:", cur.fetchone()['version'])
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Connection failed:", str(e))