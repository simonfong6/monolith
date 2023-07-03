#!/usr/bin/env python3
"""
MongoDB Client
"""
from os import environ
from urllib.parse import quote_plus

from flask import g
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from backend.observability import get_logger


logger = get_logger(__name__)


DATBASE_CONNECTION_TIMEOUT_MS = 3000


def get_client():
    host = environ['MONGO_HOST']
    user = environ['MONGO_USERNAME']
    password = environ['MONGO_PASSWORD']

    user = quote_plus(user)
    password = quote_plus(password)

    uri = f'mongodb://{user}:{password}@{host}'
    
    try:
        client = MongoClient(
            uri,
            serverSelectionTimeoutMS=DATBASE_CONNECTION_TIMEOUT_MS
        )
        client.server_info()
    except ServerSelectionTimeoutError as error:
        logger.error(f"Mongo connection failed in {DATBASE_CONNECTION_TIMEOUT_MS} milliseconds")
        print(error)
        return None

    return client


def get_database():
    name = environ['MONGO_DATABASE']

    client = get_client()
    if not client:
        logger.warning(f"No database.")
        return None

    database = client[name]

    return database

def get_flask_database():
    if 'database' not in g:
        g.database = get_database()

    return g.database
