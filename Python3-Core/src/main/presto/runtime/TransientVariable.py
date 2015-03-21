from presto.runtime.Variable import Variable


class TransientVariable ( Variable ):

	def __init__(self, name, type):
		super(TransientVariable, self).__init__(name, type)

	def __str__(self):
		return self.getName()
	
