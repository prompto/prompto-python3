from prompto.runtime.Variable import Variable
from prompto.type.EnumeratedCategoryType import EnumeratedCategoryType


class ErrorVariable ( Variable ):

	def __init__(self, name):
		super(ErrorVariable, self).__init__(name, EnumeratedCategoryType("Error"))
