from presto.error.PrestoError import PrestoError

class InternalError ( PrestoError ):

	def __init__(self, e):
		super(InternalError, self).__init__(e)
