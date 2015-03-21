from presto.python.PythonLiteral import PythonLiteral

class PythonDecimalLiteral ( PythonLiteral ):

	def __init__(self, text):
		super(PythonDecimalLiteral,self).__init__(text)
