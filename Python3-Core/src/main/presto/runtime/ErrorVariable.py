from presto.runtime.Variable import Variable
from presto.type.EnumeratedCategoryType import EnumeratedCategoryType


class ErrorVariable ( Variable ):

	def __init__(self, name):
		super(ErrorVariable, self).__init__(name, EnumeratedCategoryType("Error"))
