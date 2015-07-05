class Dialect(object):

    E = None
    O = None
    S = None

    def __init__(self, name):
        self.name = name

Dialect.E = Dialect("E")
Dialect.O = Dialect("O")
Dialect.S = Dialect("S")
	
