from presto.python.PythonLiteral import PythonLiteral

class PythonCharacterLiteral ( PythonLiteral ):

    def __init__(self, text):
        super(PythonCharacterLiteral, self).__init__(text)

