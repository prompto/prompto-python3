from prompto.value.BaseValue import BaseValue
from prompto.type.MethodType import MethodType

class ClosureValue(BaseValue):

	def __init__(self, context, itype):
		super().__init__(itype)
		self.context = context


	def interpret(self, context):
		parentMost = self.context.getParentMostContext()
		parentMost.setParentContext(context)
		result = self.itype.method.interpret(self.context)
		parentMost.setParentContext(None)
		return result

