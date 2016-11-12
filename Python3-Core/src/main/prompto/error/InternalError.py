from prompto.error.PromptoError import PromptoError

class InternalError (PromptoError):

	def __init__(self, e):
		super(InternalError, self).__init__(e)
