from presto.error.ExecutionError import ExecutionError
from presto.literal.TextLiteral import TextLiteral


class InvalidResourceError ( ExecutionError ):

    def __init__(self, message):
        super().__init__(message)

    def getExpression(self, context):
        s = self.message.replace('"',"'") # ensure TextLiteral interprets the full string
        return TextLiteral('"' + s + '"')
