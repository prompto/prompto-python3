from prompto.parser.Section import Section

class OrderByClause(Section):

    def __init__(self, names, descending):
        super().__init__()
        self.names = names
        self.descending = descending

    def toDialect(self, writer):
        for name in self.names:
            writer.append(name)
            writer.append(".")
        writer.trimLast(1)
        if self.descending:
            writer.append(" descending")
