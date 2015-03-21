from presto.value.BaseValue import BaseValue
from presto.type.MethodType import MethodType

class ClosureValue(BaseValue):

	def __init__(self, context, method):
		super().__init__(MethodType(context, method.getName()))
		self.method = method


	def interpret(self, context):
		thisContext = self.type.context
		parentMost = thisContext.getParentMostContext()
		parentMost.setParentContext(context)
		result = self.method.interpret(thisContext)
		parentMost.setParentContext(None)
		return result

