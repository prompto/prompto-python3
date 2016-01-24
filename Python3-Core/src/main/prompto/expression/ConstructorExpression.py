from io import StringIO
from prompto.expression.IExpression import IExpression
from prompto.grammar.ArgumentAssignment import ArgumentAssignment
from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import Context
from prompto.type.IType import IType
from prompto.value.IInstance import IInstance
from prompto.error.SyntaxError import SyntaxError
from prompto.error.NotMutableError import NotMutableError

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
            if self.mutable:
                sb.write("mutable ")
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
        self.type.toDialect(writer)
        if self.copyFrom is not None:
            writer.append(" from ")
            writer.append(str(self.copyFrom))
            if self.assignments is not None and len(self.assignments)>0:
                writer.append(",")
        if self.assignments is not None:
            self.assignments.toDialect(writer)

    def toODialect(self, writer):
        self.type.toDialect(writer)
        assignments = ArgumentAssignmentList()
        if self.copyFrom is not None:
            assignments.append(ArgumentAssignment(None, self.copyFrom))
        if self.assignments is not None:
            assignments.extend(self.assignments)
        assignments.toDialect(writer)

    def toSDialect(self, writer):
        self.toODialect(writer)

    def check(self, context:Context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.type.CategoryType import CategoryType
        cd = context.getRegisteredDeclaration(CategoryDeclaration, self.type.getName())
        if cd is None:
            raise SyntaxError("Unknown category " + self.type.getName())
        type = cd.getType(context)
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
        return type

    def interpret(self, context:Context):
        instance = self.type.newInstance(context)
        instance.mutable = True
        if self.copyFrom is not None:
            copyObj = self.copyFrom.interpret(context)
            if isinstance(copyObj, IInstance):
                from prompto.declaration.CategoryDeclaration import CategoryDeclaration
                cd = context.getRegisteredDeclaration(CategoryDeclaration, self.type.getName())
                for name in copyObj.getAttributeNames():
                    if cd.hasAttribute(context, name):
                        value = copyObj.GetMember(context,name)
                        if value is not None and value.mutable and not self.type.mutable:
                            raise NotMutableError()
                        instance.SetMember(context, name, value)
        if self.assignments is not None:
            for assignment in self.assignments:
                value = assignment.getExpression().interpret(context)
                if value is not None and value.mutable and not self.type.mutable:
                    raise NotMutableError()
                instance.SetMember(context, assignment.getName(), value)
        instance.mutable = self.type.mutable
        return instance
