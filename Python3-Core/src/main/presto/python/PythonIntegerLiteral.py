from presto.python.PythonLiteral import PythonLiteral

class PythonIntegerLiteral ( PythonLiteral ):

	def __init__(self, text):
		super(PythonIntegerLiteral,self).__init__(text)
