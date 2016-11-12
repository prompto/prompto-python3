from prompto.value.BaseValue import BaseValue
from prompto.type.MethodType import MethodType

class ClosureValue(BaseValue):

	def __init__(self, context, typ):
		super().__init__(typ)
		self.context = context


	def interpret(self, context):
		parentMost = self.context.getParentMostContext()
		parentMost.setParentContext(context)
		result = self.type.method.interpret(self.context)
		parentMost.setParentContext(None)
		return result

