#!/usr/bin/env python3
"""
Database Client
"""
from os import environ
from urllib.parse import quote_plus

import psycopg2
from flask import g

from backend.observability import get_logger


logger = get_logger(__name__)


DATBASE_CONNECTION_TIMEOUT_MS = 3000
POSTGRES_PORT = 5432


def get_client():
    host = environ['POSTGRES_HOST']
    username = environ['POSTGRES_USERNAME']
    password = environ['POSTGRES_PASSWORD']
    database = environ['POSTGRES_DATABASE']

    conn = psycopg2.connect(
        host=host, port=POSTGRES_PORT, database=database, user=username,
        password=password)

    return conn


def get_flask_database():
    if 'database' not in g:
        g.database = get_client()

    return g.database
