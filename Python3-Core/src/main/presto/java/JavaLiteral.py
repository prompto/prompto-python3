from presto.java.JavaExpression import JavaExpression

class JavaLiteral (JavaExpression):

    def __init__(self, text):
        super(JavaLiteral,self).__init__(text)

    def toDialect(self, writer):
        writer.append(self.text)
