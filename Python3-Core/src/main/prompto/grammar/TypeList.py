class TypeList ( list ):

	def __init__(self, itype):
		super(TypeList, self).__init__()
		if itype is not None:
			self.append(itype)
