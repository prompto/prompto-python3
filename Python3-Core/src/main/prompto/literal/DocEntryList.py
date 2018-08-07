from io import StringIO

class DocEntryList ( list ):

    def __init__(self, entry = None, entries = None):
        if entries is not None:
            super().__init__(entries)
        else:
            super().__init__()
        if entry is not None:
            self.append(entry)


    def __str__(self):
        with StringIO() as sb:
            sb.write('{')
            for item in self:
                sb.write(str(item))
                sb.write(", ")
            slen = sb.tell()
            if slen>2:
                sb.truncate(slen-2)
                sb.seek(slen-2)
            sb.write('}')
            return sb.getvalue()


    def toDialect(self, writer):
        writer.append('{')
        if len(self)>0:
            for entry in self:
                entry.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)
        writer.append('}')
