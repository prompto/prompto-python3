from io import StringIO
from presto.grammar.IDialectElement import IDialectElement


class ArgumentAssignmentList(list, IDialectElement):

    def __init__(self, list_=None, item=None):
        if list_ == None:
            super(ArgumentAssignmentList, self).__init__()
        else:
            super(ArgumentAssignmentList, self).__init__(list_)
        if item != None:
            self.append(item)

    def find(self, name):
        for assignment in self:
            if name == assignment.getName():
                return assignment
        return None

    def makeAssignments(self, context, declaration):
        assignments = ArgumentAssignmentList()
        for assignment in self:
            assignments.append(assignment.makeAssignment(context, declaration))
        return assignments

    def __str__(self):
        li = self
        with StringIO() as sb:
            idx = 0
            # anonymous argument before 'with'
            if len(li) > 0 and li[0].getArgument() is None:
                sb.write(' ')
                sb.write(str(li[idx]))
                idx += 1
            if idx < len(li):
                sb.write(" with ")
                sb.write(str(li[idx]))
                idx += 1
                sb.write(", ")
                while idx < len(li) - 1:
                    sb.write(str(li[idx]))
                    idx += 1
                    sb.write(", ")
                slen = sb.tell()
                sb.truncate(slen - 2)
                sb.seek(slen - 2)
                if idx < len(li):
                    sb.write(" and ")
                    sb.write(str(li[idx]))
            return sb.getvalue()

    def toEDialect(self, writer):
        idx = 0
        # anonymous argument before 'with'
        if len(self)>0 and self[0].argument is None:
            writer.append(' ')
            self[idx].toDialect(writer)
            idx += 1
        if idx<len(self):
            writer.append(" with ")
            self[idx].toDialect(writer)
            idx += 1
            writer.append(", ")
            while idx<len(self)-1:
                self[idx].toDialect(writer)
                idx += 1
                writer.append(", ")
            writer.trimLast(2)
            if idx<len(self):
                writer.append(" and ")
                self[idx].toDialect(writer)

    def toODialect(self, writer):
        writer.append("(")
        for arg in self:
            arg.toDialect(writer)
            writer.append(", ")
        if len(self)>0:
            writer.trimLast(2)
        writer.append(")")

    def toSDialect(self, writer):
        self.toODialect(writer)
