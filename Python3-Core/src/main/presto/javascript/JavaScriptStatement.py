class JavaScriptStatement(object):

    def __init__(self, expression, isReturn):
        self.expression = expression
        self.isReturn = isReturn
        self.module = None

    def __str__(self):
        return ("return " if self.isReturn else "") + str(self.expression) + ";"

    def toDialect(self, writer):
        if self.isReturn:
            writer.append("return ")
        self.expression.toDialect(writer)
        writer.append(';')
        if self.module is not None:
            self.module.toDialect(writer)
