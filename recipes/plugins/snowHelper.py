
from snowfakery import SnowfakeryPlugin


class SnowPunnary(SnowfakeryPlugin):
    class Functions:
        def snowpunner(self, word):
            return 'Snow' + word + 'ary'

        def currentCounter(self):
            context_vars = self.context.context_vars()
            context_vars.setdefault("count", 0)
            context_vars["count"] += 1
            return context_vars["count"]
