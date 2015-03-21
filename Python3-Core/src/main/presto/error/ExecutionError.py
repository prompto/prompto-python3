from presto.error.PrestoError import PrestoError


class ExecutionError(PrestoError):

    def __init__(self, message=None, exception=None):
        super().__init__(message, exception)
