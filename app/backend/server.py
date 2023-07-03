#!/usr/bin/env python3
"""
Backend server.
"""
import logging
import time

from flask import Flask
from flask import send_from_directory
import psycopg2

from backend.api import register_sub_site
from backend.database.json import CustomJSONEncoder
from backend.database.seed import main


# Configure logging.
logging.basicConfig(filename='server.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


app = Flask(
    __name__,
    static_folder='/code/build',  # Serve the React files.
    static_url_path='/'
)
app.json_encoder = CustomJSONEncoder
register_sub_site(app)

# Allow fetching root serves index file.
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/time')
def get_current_time():
    logger.info("Time")
    return {
        'time': time.time(),
        'status': 'success',
        'version': 1
    }

@app.route('/seed')
def seed():
    logger.info("Seed")
    main()
    return {
        'message': 'Seeding database.'
    }

@app.route('/databaselistusers')
def databaselistusers():
    from os import environ
    host = environ['POSTGRES_HOST']
    username = environ['POSTGRES_USERNAME']
    password = environ['POSTGRES_PASSWORD']
    msg = "words " + ','.join([host, username, password])

    conn = psycopg2.connect(host=host, port = 5432, database="monolith", user=username, password=password)

    # Create a cursor object
    cur = conn.cursor()

    # A sample query of all data from the "vendors" table in the "suppliers" database
    cur.execute("""SELECT * FROM users""")
    query_results = cur.fetchall()
    res = str(query_results)
    print(res)

    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests
    cur.close()
    conn.close()

    return {
        'status': 'success',
        'msg': f'{msg}',
        'result': res,
        'results': query_results
    }
