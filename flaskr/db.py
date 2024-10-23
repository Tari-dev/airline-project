import sqlite3
import atexit

from flask import  g, current_app

__all__ = ('get_db', 'get_cursor', 'close_db')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('airline.db', detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        current_app.db = g.db

    return g.db


@atexit.register
def close_db():
    db = g.pop('db', None)

    if db:
        db.close()