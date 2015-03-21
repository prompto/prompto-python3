class CmpOp (object):
    GT = None
    GTE = None
    LT = None
    LTE = None

    def __init__(self, text):
        self.text = text

    def toDialect(self, writer):
        writer.append(self.text)

CmpOp.GT = CmpOp(">")
CmpOp.GTE = CmpOp(">=")
CmpOp.LT = CmpOp("<")
CmpOp.LTE = CmpOp("<=")

