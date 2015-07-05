class ContOp(object):
    IN = None
    CONTAINS = None
    CONTAINS_ALL = None
    CONTAINS_ANY = None
    NOT_IN = None
    NOT_CONTAINS = None
    NOT_CONTAINS_ALL = None
    NOT_CONTAINS_ANY = None

    def __init__(self, name):
        self.name = name

    def toDialect(self, writer):
        writer.append(self.name.lower().replace('_', ' '))


ContOp.IN = ContOp("IN")
ContOp.CONTAINS = ContOp("CONTAINS")
ContOp.CONTAINS_ALL = ContOp("CONTAINS_ALL")
ContOp.CONTAINS_ANY = ContOp("CONTAINS_ANY")
ContOp.NOT_IN = ContOp("NOT_IN")
ContOp.NOT_CONTAINS = ContOp("NOT_CONTAINS")
ContOp.NOT_CONTAINS_ALL = ContOp("NOT_CONTAINS_ALL")
ContOp.NOT_CONTAINS_ANY = ContOp("NOT_CONTAINS_ANY")

