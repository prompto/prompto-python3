from presto.error.PrestoError import PrestoError

class SyntaxError ( PrestoError ):

    def __init__(self, message):
        super().__init__(message)
