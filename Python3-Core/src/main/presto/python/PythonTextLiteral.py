from presto.python.PythonLiteral import PythonLiteral


class PythonTextLiteral(PythonLiteral):

    def __init__(self, text):
        super(PythonTextLiteral, self).__init__(text)
