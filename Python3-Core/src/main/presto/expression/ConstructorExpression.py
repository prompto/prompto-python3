from io import StringIO
from presto.expression.IExpression import IExpression
from presto.grammar.ArgumentAssignment import ArgumentAssignment
from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from presto.parser.Dialect import Dialect
from presto.runtime.Context import Context
from presto.type.IType import IType
from presto.value.IInstance import IInstance
from presto.error.SyntaxError import SyntaxError

class ConstructorExpression(IExpression):

    def __init__(self, type:IType, assignments:ArgumentAssignmentList):
        self.copyFrom = None
        self.type = type
        self.setAssignments(assignments)

    def getType(self):
        return self.type

    def setAssignments(self, assignments:ArgumentAssignmentList):
        self.assignments = assignments
        # in OOPS, first anonymous argument is copyFrom
        if assignments is not None and len(assignments)>0 and assignments[0].getArgument() is None:
            self.copyFrom = assignments[0].getExpression()
            self.assignments.pop(0)

    def getAssignments(self):
        return self.assignments

    def setCopyFrom(self, copyFrom:IExpression):
        self.copyFrom = copyFrom

    def getCopyFrom(self):
        return self.copyFrom

    def __str__(self):
        with StringIO() as sb:
            sb.write(self.type.getName())
            sb.write(' ')
            if self.copyFrom is not None:
                sb.write("(from:")
                sb.write(str(self.copyFrom))
                sb.write(") ")
            if self.assignments is not None:
                sb.write("with ")
                sb.write(str(self.assignments))
            return sb.getvalue()

    def toEDialect(self, writer):
        writer.append(self.type.getName())
        if self.copyFrom is not None:
            writer.append(" from ")
            writer.append(str(self.copyFrom))
            if self.assignments is not None and len(self.assignments)>0:
                writer.append(",")
        if self.assignments is not None:
            self.assignments.toDialect(writer)

    def toODialect(self, writer):
        writer.append(self.type.getName())
        assignments = ArgumentAssignmentList()
        if self.copyFrom is not None:
            assignments.append(ArgumentAssignment(None, self.copyFrom))
        if self.assignments is not None:
            assignments.extend(self.assignments)
        assignments.toDialect(writer)

    def toPDialect(self, writer):
        self.toODialect(writer)

    def check(self, context:Context):
        from presto.declaration.CategoryDeclaration import CategoryDeclaration
        from presto.type.CategoryType import CategoryType
        cd = context.getRegisteredDeclaration(CategoryDeclaration, self.type.getName())
        if cd is None:
            raise SyntaxError("Unknown category " + self.type.getName())
        self.type = cd.getType(context)
        cd.checkConstructorContext(context)
        if self.copyFrom is not None:
            cft = self.copyFrom.check(context)
            if not isinstance(cft, CategoryType):
                raise SyntaxError("Cannot copy from " + cft.getName())
        if self.assignments is not None:
            for assignment in self.assignments:
                if not cd.hasAttribute(context, assignment.getName()):
                    raise SyntaxError("\"" + assignment.getName() +
                        "\" is not an attribute of " + self.type.getName())
                assignment.check(context)
        return self.type

    def interpret(self, context:Context):
        instance = self.type.newInstance(context)
        if self.copyFrom is not None:
            copyObj = self.copyFrom.interpret(context)
            if isinstance(copyObj, IInstance):
                from presto.declaration.CategoryDeclaration import CategoryDeclaration
                cd = context.getRegisteredDeclaration(CategoryDeclaration, self.type.getName())
                for name in copyObj.getAttributeNames():
                    if cd.hasAttribute(context, name):
                        instance.set(context, name, copyObj.getMember(context,name))
        if self.assignments is not None:
            for assignment in self.assignments:
                value = assignment.getExpression().interpret(context)
                instance.set(context, assignment.getName(), value)
        return instance
