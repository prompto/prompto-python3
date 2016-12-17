from prompto.utils.ObjectList import ObjectList
from io import StringIO


class SymbolList (ObjectList):

    def __init__(self, symbol = None):
        super(SymbolList, self).__init__()
        if symbol is not None:
            self.append(symbol)



    def __str__(self):
        sb = StringIO()
        sb.write("[")
        for item in self:
            sb.write(item.getName())
            sb.write(", ")
        slen = sb.tell()
        sb.truncate(slen - 2)
        sb.seek(slen - 2)
        sb.write("]")
        return sb.getvalue()