#!/usr/bin/env python3
"""
Database Seeding

Thanks to this blog:
https://phauer.com/2018/local-development-docker-compose-seeding-stubs/
"""
import random

from bson.objectid import ObjectId
from faker import Faker

from backend.database import get_database
from backend.observability import get_logger


logger = get_logger(__name__)


POSSIBLE_TAGS = ['vacation', 'business', 'technology', 'mobility', 'apparel']
faker = Faker('en')


class MongoSeeder:

    def __init__(self):
        self.db = get_database()

    def seed(self):
        if not self.db:
            logger.warning("No database to seed.")
            return
        logger.info('Clearing collection...')
        self.db.posts.delete_many({})
        logger.info('Inserting new data...')
        posts = [generate_post() for _ in range(5)]
        self.db.posts.insert_many(posts)
        logger.info('Done.')


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
    MongoSeeder().seed()


if __name__ == '__main__':
    main()
