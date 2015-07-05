from io import StringIO

class CSharpExpressionList (list):

    def __init__(self, item = None):
        if item is not None:
            self.append(item)

    def __str__(self):
        with StringIO() as sb:
            for item in self:
                sb.write(item)
                sb.write(", ")
            if sb.len>=2:
                sb.truncate(sb.len-2)
            return sb.getvalue()

    def toDialect(self, writer):
        for item in self:
            item.toDialect(writer)
            writer.append(", ")
        if len(self)>0:
            writer.trimLast(2)
