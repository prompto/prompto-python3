class CategoryMethodDeclarationList (list):

	def __init__(self, method = None):
		super(CategoryMethodDeclarationList, self).__init__()
		if method is not None:
			self.append(method)
