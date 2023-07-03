#!/usr/bin/env python3
"""
Posts Blueprint
"""
from flask import Blueprint
from flask import jsonify
from flask import request

from backend.database import get_flask_database
from backend.observability import get_logger


logger = get_logger(__name__)


posts = Blueprint('posts', __name__)


@posts.route('/')
def index():
    db = get_flask_database()
    posts = db.posts

    cursor = posts.find({})
    docs = []
    for document in cursor:
        docs.append(document)
        logger.info(document)
    return jsonify(docs)

@posts.route('/new')
def create():
    db = get_flask_database()
    posts = db.posts

    import datetime

    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    }

    post_id = posts.insert_one(post).inserted_id

    post = posts.find_one({"_id": post_id})
    logger.info(post)

    return jsonify(post)

@posts.route('/author')
def fetch_by_author():
    db = get_flask_database()
    posts = db.posts

    author = request.args['author']

    post = posts.find_one({"author": author})

    return jsonify(post)

@posts.route('/justin')
def justin():

    return jsonify({
        "Suck": "Butt"
    })

@posts.route('/factorial/<num>')
def factorial(num):
    num = int(num)
    product = 1
    for num in range(1, num + 1):
	    product *= num  
    return jsonify({
        "answer": product
    })
