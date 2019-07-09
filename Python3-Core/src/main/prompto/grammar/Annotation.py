class Annotation(object):

    def __init__(self, name, entries):
        self.name = name
        self.entries = entries


    def toDialect(self, writer):
        writer.append(self.name)
        if self.entries is not None and len(self.entries) > 0:
            writer.append("(")
            for entry in self.entries:
                if entry.key is not None:
                    writer.append(entry.key)
                    writer.append(" = ")
                entry.value.toDialect(writer)
                writer.append(", ")
            writer.trimLast(len(", "))
            writer.append(")")
        writer.newLine()
