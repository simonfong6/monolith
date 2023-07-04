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
    conn = get_flask_database()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM public.posts""")
    posts = cur.fetchall()

    docs = []
    for document in posts:
        docs.append(document)
        logger.info(document)
    return jsonify(docs)


@posts.route('/new')
def create():
    conn = get_flask_database()
    cur = conn.cursor()

    import datetime

    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["postgres", "python", "psycopg2"],
        "date": datetime.datetime.utcnow()
    }

    tags = post['tags']
    tags = map(lambda tag: f"'{tag}'", tags)
    tags = ','.join(tags)
    cur.execute(f"""
INSERT INTO public.posts(
	author, text, tags, date)
	VALUES (
        '{post['author']}',
        '{post['text']}',
        ARRAY[{tags}]::text[],
        '{post['date']}') RETURNING id;
    """)
    result = cur.fetchone()
    logger.info(result)

    cur.execute(f"""
SELECT id, author, text, tags, date FROM public.posts
WHERE id = {result[0]};""")
    
    post = cur.fetchone()

    conn.commit()

    logger.info(post)

    return jsonify(post)


@posts.route('/author')
def fetch_by_author():
    conn = get_flask_database()
    cur = conn.cursor()

    author = request.args['author']
    cur.execute(f"""SELECT * FROM public.posts WHERE author = '{author}'""")
    post = cur.fetchone()

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
