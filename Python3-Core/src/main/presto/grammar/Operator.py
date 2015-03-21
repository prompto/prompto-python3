class Operator (object):

    PLUS = None
    MINUS = None
    MULTIPLY = None
    DIVIDE = None
    IDIVIDE = None
    MODULO = None

    def __init__(self, name, token):
        self.name = name
        self.token = token

    def toDialect(self, writer):
        writer.append(self.token)

Operator.PLUS = Operator("PLUS", "+")
Operator.MINUS = Operator("MINUS", "-")
Operator.MULTIPLY = Operator("MULTIPLY", "*")
Operator.DIVIDE = Operator("DIVIDE", "/")
Operator.IDIVIDE = Operator("IDIVIDE", "\\")
Operator.MODULO = Operator("MODULO", "%")

