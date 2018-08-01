class Annotation(object):

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression


    def toDialect(self, writer):
        writer.append(self.name)
        if self.expression is not None:
            writer.append("(")
            self.expression.toDialect(writer)
            writer.append(")")
        writer.newLine()
