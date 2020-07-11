from prompto.error.PromptoError import PromptoError

class SyntaxError (PromptoError):

    def __init__(self, message):
        super().__init__(message)
        self.suffix = ""


    def __getattribute__(self, item):
        value = super().__getattribute__(item)
        if item == "message":
            return value + self.suffix
        else:
            return value
