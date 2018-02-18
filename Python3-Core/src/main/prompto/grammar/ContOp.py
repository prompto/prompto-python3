class ContOp(object):
    IN = None
    HAS = None
    HAS_ALL = None
    HAS_ANY = None
    NOT_IN = None
    NOT_HAS = None
    NOT_HAS_ALL = None
    NOT_HAS_ANY = None

    def __init__(self, name):
        self.name = name

    def toDialect(self, writer):
        writer.append(self.name.lower().replace('_', ' '))


ContOp.IN = ContOp("IN")
ContOp.HAS = ContOp("HAS")
ContOp.HAS_ALL = ContOp("HAS_ALL")
ContOp.HAS_ANY = ContOp("HAS_ANY")
ContOp.NOT_IN = ContOp("NOT_IN")
ContOp.NOT_HAS = ContOp("NOT_HAS")
ContOp.NOT_HAS_ALL = ContOp("NOT_HAS_ALL")
ContOp.NOT_HAS_ANY = ContOp("NOT_HAS_ANY")

