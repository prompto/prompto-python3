from io import StringIO

from prompto.param.AttributeParameter import AttributeParameter
from prompto.expression.AndExpression import AndExpression
from prompto.grammar.Argument import Argument
from prompto.grammar.IDialectElement import IDialectElement


class ArgumentList(list, IDialectElement):

    def __init__(self, items=None):
        if items == None:
            super(ArgumentList, self).__init__()
        else:
            super(ArgumentList, self).__init__(items)

    # post - fix expression priority for final assignment in E dialect
    # 'xyz with a and b as c' should read 'xyz with a, b as c' NOT 'xyz with (a and b) as c'
    def checkLastAnd(self):
        assignment = self[-1]
        if assignment is not None and assignment.getParameter() is not None and isinstance(assignment.getExpression(), AndExpression):
            _and = assignment.getExpression()
            from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
            if isinstance(_and.left, UnresolvedIdentifier):
                name = _and.left.name
                if name[0].islower():
                    del self[-1]
                    # add AttributeArgument
                    argument = AttributeParameter(name)
                    attribute = Argument(argument, None)
                    self.append(attribute)
                    # fix last assignment
                    assignment.setExpression( _and.right)
                    self.append(assignment)

    def find(self, name):
        for assignment in self:
            if name == assignment.getName():
                return assignment
        return None


    def makeAssignments(self, context, declaration):
        assignments = ArgumentList()
        for assignment in self:
            assignments.append(assignment.makeArgument(context, declaration))
        return assignments


    def __str__(self):
        li = self
        with StringIO() as sb:
            idx = 0
            # anonymous argument before 'with'
            if len(li) > 0 and li[0].getParameter() is None:
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

    def toMDialect(self, writer):
        self.toODialect(writer)
