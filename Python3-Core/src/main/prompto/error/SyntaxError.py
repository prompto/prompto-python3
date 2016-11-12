from prompto.error.PromptoError import PromptoError

class SyntaxError (PromptoError):

    def __init__(self, message):
        super().__init__(message)
