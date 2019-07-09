class Annotation(object):

    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


    def toDialect(self, writer):
        writer.append(self.name)
        if self.arguments is not None and len(self.arguments) > 0:
            writer.append("(")
            for entry in self.arguments:
                if entry.key is not None:
                    writer.append(entry.key)
                    writer.append(" = ")
                entry.value.toDialect(writer)
                writer.append(", ")
            writer.trimLast(len(", "))
            writer.append(")")
        writer.newLine()
