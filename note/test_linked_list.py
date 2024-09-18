class Link:
    empty= ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest == ():
            return "Link({0})".format(self.first)
        return "Link({0}, {1})".format(self.first, self.rest)