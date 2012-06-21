# -*- coding:utf-8 -*-

from mongokit import Connection, Document
from flask import g, current_app as app

def get_connection():
    """Get connection handler"""
    models = []
    connection = getattr(g, 'db_connection', None)
    if connection is None:
        g.db_connection = Connection(app.config['MONGODB_HOST'],
                                     app.config['MONGODB_PORT'])
        g.db_connection.register(models)
        return g.db_connection
    return connection

def get_db():
    """Get database handler"""
    db = getattr(g, 'db', None)
    if db is None:
        connection = get_connection()
        db = g.db = connection[app.config['MONGODB_DATABASE']]
    return db
