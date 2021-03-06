from prompto.value.BaseValue import BaseValue

class ClosureValue(BaseValue):

	def __init__(self, context, itype):
		super().__init__(itype)
		self.context = context


	def interpret(self, context):
		parentMost = self.context.getParentMostContext()
		savedParent = parentMost.getParentContext()
		if not context.isChildOf(parentMost):
			parentMost.setParentContext(context)
		try:
			local = self.context.newChildContext()
			return self.doInterpret(local)
		finally:
			parentMost.setParentContext(savedParent)


	def doInterpret(self, local):
		return self.itype.method.interpret(local)


	def convertToPython(self):
		return self
