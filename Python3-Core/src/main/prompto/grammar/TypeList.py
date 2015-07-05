class TypeList ( list ):

	def __init__(self, type_):
		super(TypeList, self).__init__()
		if type_ is not None:
			self.append(type_)
