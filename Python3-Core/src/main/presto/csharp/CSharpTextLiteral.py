from presto.csharp.CSharpLiteral import CSharpLiteral

class CSharpTextLiteral ( CSharpLiteral ):

	def __init__(self, text):
		super(CSharpTextLiteral,self).__init__(text)
