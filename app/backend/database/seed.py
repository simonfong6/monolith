#!/usr/bin/env python3
"""
Database Seeding

Thanks to this blog:
https://phauer.com/2018/local-development-docker-compose-seeding-stubs/
"""
import random

from faker import Faker

from backend.database import get_client
from backend.observability import get_logger


logger = get_logger(__name__)


POSSIBLE_TAGS = ['vacation', 'business', 'technology', 'mobility', 'apparel']
faker = Faker('en')


class DatabaseSeeder:

    def __init__(self):
        self.conn = get_client()

    def create_table(self):
        if not self.conn:
            logger.warning("No database to seed.")
            return

        cur = self.conn.cursor()
        cur.execute("""
CREATE TABLE IF NOT EXISTS public.posts (
   id SERIAL PRIMARY KEY,
   author TEXT,
   text TEXT,
   tags TEXT[],
   date TIMESTAMP
);
        """)
        cur.close()
        self.conn.commit()

    def seed(self):
        if not self.conn:
            logger.warning("No database to seed.")
            return
        self.create_table()

        cur = self.conn.cursor()
        cur.execute("""
TRUNCATE TABLE public.posts;
        """)
        for _ in range(5):
            post = generate_post()
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
        '{post['date']}');
            """)
        cur.close()
        self.conn.commit()


def choose_max_n_times(possibilities, max_n):
    copied_list = list(possibilities)
    random.shuffle(copied_list)
    n = random.randint(0, max_n)
    chosen = [copied_list.pop() for _ in range(n)]
    return chosen


def generate_post():
    data = {
        "author": faker.name(),
        "text": faker.sentence(nb_words=7),
        "tags": choose_max_n_times(possibilities=POSSIBLE_TAGS, max_n=3),
        "date": faker.date_time()
    }
    return data


def main():
    Faker.seed(0)
    DatabaseSeeder().seed()


if __name__ == '__main__':
    main()
