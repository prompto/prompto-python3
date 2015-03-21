from presto.python.PythonExpression import PythonExpression

class PythonLiteral (PythonExpression):

    def __init__(self, text):
        super(PythonLiteral,self).__init__()
        self.text = text
        self.value = eval(compile(text, "__no_file__", mode='eval'))

    def interpret(self, context, module):
        return self.value

    def __str__(self):
        return self.text

    def toDialect(self, writer):
        writer.append(self.text)
