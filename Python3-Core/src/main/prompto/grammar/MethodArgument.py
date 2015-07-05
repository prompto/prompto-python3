from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.grammar.BaseArgument import BaseArgument
from prompto.grammar.INamedArgument import INamedArgument
from prompto.grammar.INamedValue import INamedValue
from prompto.type.MethodType import MethodType


class MethodArgument ( BaseArgument, INamedArgument ):
	
	def __init__(self, name):
		super(MethodArgument, self).__init__(name)
	
	def getSignature(self, dialect):
		return self.getName()

	def __str__(self):
		return self.getName()
	
	def getProto(self, context):
		return self.getName()
	
	def __eq__(self, obj):
		if id(obj)==id(self):
			return True
		if obj is None:
			return False
		if not isinstance(obj, MethodArgument):
			return False
		return self.getName()==obj.getName()

	def register(self, context):
		actual = context.getRegisteredValue(INamedValue,self.name)
		if actual is not None:
			raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
		context.registerValue(self)
	
	def check(self, context):
		actual = context.getRegisteredDeclaration(IMethodDeclaration,self.name)
		if actual is None:
			raise SyntaxError("Unknown method: \"" + self.name + "\"")
	
	def getType(self, context):
		return MethodType(context,self.name)
