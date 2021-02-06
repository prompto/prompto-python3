class Specificity(object):

	INCOMPATIBLE = None
	RESOLVED = None
	INHERITED = None
	EXACT = None
	
	def __init__(self, idx):
		self.idx = idx
		
	def greaterThan(self, other):
		return self.idx > other.idx
	
Specificity.INCOMPATIBLE = Specificity(0)
Specificity.INHERITED = Specificity(1)
Specificity.EXACT = Specificity(2)
Specificity.DERIVED = Specificity(3)
