from prompto.utils.ObjectList import ObjectList
from prompto.parser.Dialect import Dialect

class OrderByClauseList(ObjectList):

    def __init__(self, clause = None):
        super().__init__()
        if clause is not None:
            self.append(clause)

    def toDialect(self, writer):
        writer.append("order by ")
        if writer.dialect is Dialect.O:
            writer.append("( ")
        for clause in self:
            clause.toDialect(writer)
            writer.append(", ")
        writer.trimLast(2)
        if writer.dialect is Dialect.O:
            writer.append(" )")
