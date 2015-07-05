from prompto.utils.ObjectList import ObjectList


class JavaScriptExpressionList (ObjectList):


    def __init__(self, expression):
        super(JavaScriptExpressionList, self).__init__()
        if expression is not None:
            self.append(expression)

    def toDialect(self, writer):
        if len(self)>0:
            for exp in self:
                exp.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)
