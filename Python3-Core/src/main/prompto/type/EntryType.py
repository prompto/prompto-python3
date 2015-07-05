from prompto.type.BaseType import BaseType
from prompto.type.TextType import TextType


class EntryType ( BaseType ):

	def __init__(self, itemType):
		super(EntryType, self).__init__(itemType.getName() + "{}[]")
		self.itemType = itemType

	def getItemType(self):
		return self.itemType

	def checkMember(self, context, name):
		if "key"==name:
			return TextType.instance
		elif "value"==name:
			return self.itemType
		else:
			return super(EntryType, self).checkMember(context, name)
