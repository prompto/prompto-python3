from io import StringIO

class JavaExpressionList (list):

    def __init__(self, item = None):
        if item is not None:
            self.append(item)

    def __str__(self):
        with StringIO() as sb:
            for item in self:
                sb.write(str(item))
                sb.write(", ")
            len = sb.tell()
            if len>0:
                sb.truncate(len-2)
            return sb.getvalue()

    def toDialect(self, writer):
        for item in self:
            item.toDialect(writer)
            writer.append(", ")
        if len(self)>0:
            writer.trimLast(2)