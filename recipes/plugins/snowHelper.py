
from snowfakery import SnowfakeryPlugin


class SnowPunnary(SnowfakeryPlugin):
    class Functions:
        def snowpunner(self, word):
            return 'Snow' + word
