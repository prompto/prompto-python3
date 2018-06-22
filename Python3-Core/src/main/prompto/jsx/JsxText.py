from prompto.jsx.IJsxExpression import IJsxExpression

from prompto.type.TextType import TextType


class JsxText(IJsxExpression):

	def __init__(self, text):
		super().__init__()
		self.text = text


	def check(self, context):
		return TextType.instance


	def toDialect(self, writer):
		writer.append(self.text)
