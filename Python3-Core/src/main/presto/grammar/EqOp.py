class EqOp (object):

    IS = None
    IS_NOT = None
    IS_A = None
    IS_NOT_A = None
    EQUALS = None
    NOT_EQUALS = None
    ROUGHLY = None

    def __init__(self, e, o, s):
        self.E = e
        self.O = o
        self.S = s

    def toDialect(self, writer):
        writer.append(self.toString(writer.dialect))

    def toString(self, dialect):
        return getattr(self, dialect.name)

EqOp.IS = EqOp("is", "is", "is")
EqOp.IS_NOT = EqOp("is not", "is not", "is not")
EqOp.IS_A = EqOp("is a", "is a", "is a")
EqOp.IS_NOT_A = EqOp("is not a", "is not a", "is not a")
EqOp.EQUALS = EqOp("=", "==", "==")
EqOp.NOT_EQUALS = EqOp("<>", "!=", "!=")
EqOp.ROUGHLY = EqOp("~", "~=", "~=")
