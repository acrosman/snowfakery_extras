
from snowfakery import SnowfakeryPlugin
import random


class SnowPunnary(SnowfakeryPlugin):
    class Functions:
        def products(self):
            products = ['Docker', 'Drupal', 'WordPress', 'Postgres', 'MySQL']
            suffixes = ['y', 'izer']
            return "".join('Snow', random.choice(products), random.choice(suffixes))
