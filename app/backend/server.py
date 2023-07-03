#!/usr/bin/env python3
"""
Backend server.
"""
import logging
import time

from flask import Flask
from flask import send_from_directory

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
        'version': 0.11
    }

@app.route('/seed')
def seed():
    logger.info("Seed")
    main()
    return {
        'message': 'Seeding database.'
    }
