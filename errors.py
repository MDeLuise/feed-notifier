class UserError(Exception):
    def __init__(self, link):
        self._link = link

    def __str__(self):
        return "error fetching link %s" % self._link
