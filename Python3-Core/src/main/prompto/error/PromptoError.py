class PromptoError (Exception):

    def __init__(self, message = None, exception = None):
        super().__init__()
        self.message = message
        self.exception = exception
