from io import StringIO

class PythonExpressionList (list):

    def __init__(self, item = None):
        if item is not None:
            self.append(item)

    def __str__(self):
        with StringIO() as sb:
            for item in self:
                sb.write(item)
                sb.write(", ")
            len = sb.tell()
            if len>=2:
                sb.truncate(len-2)
                sb.seek(len-2)
            return sb.getvalue()

