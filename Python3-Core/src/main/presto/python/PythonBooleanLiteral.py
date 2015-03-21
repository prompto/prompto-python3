from presto.python.PythonLiteral import PythonLiteral

class PythonBooleanLiteral ( PythonLiteral ):

    def __init__(self, text):
        super(PythonBooleanLiteral, self).__init__(text)

