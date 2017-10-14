from io import StringIO
from prompto.expression.IExpression import IExpression
from prompto.grammar.ArgumentAssignment import ArgumentAssignment
from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from prompto.runtime.Context import Context
from prompto.type.DocumentType import DocumentType
from prompto.type.IType import IType
from prompto.value.Document import Document
from prompto.value.IInstance import IInstance
from prompto.error.SyntaxError import SyntaxError
from prompto.error.NotMutableError import NotMutableError

class ConstructorExpression(IExpression):

    def __init__(self, itype:IType, assignments:ArgumentAssignmentList):
        self.copyFrom = None
        self.mutable = False
        self.itype = itype
        self.setAssignments(assignments)

    def getType(self):
        return self.itype

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
            sb.write(self.itype.typeName)
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
        self.itype.toDialect(writer)
        if self.copyFrom is not None:
            writer.append(" from ")
            writer.append(str(self.copyFrom))
            if self.assignments is not None and len(self.assignments)>0:
                writer.append(",")
        if self.assignments is not None:
            self.assignments.toDialect(writer)

    def toODialect(self, writer):
        self.itype.toDialect(writer)
        assignments = ArgumentAssignmentList()
        if self.copyFrom is not None:
            assignments.append(ArgumentAssignment(None, self.copyFrom))
        if self.assignments is not None:
            assignments.extend(self.assignments)
        assignments.toDialect(writer)

    def toMDialect(self, writer):
        self.toODialect(writer)

    def check(self, context:Context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.type.CategoryType import CategoryType
        cd = context.getRegisteredDeclaration(CategoryDeclaration, self.itype.typeName)
        if cd is None:
            raise SyntaxError("Unknown category " + self.itype.typeName)
        itype = cd.getType(context)
        cd.checkConstructorContext(context)
        if self.copyFrom is not None:
            cft = self.copyFrom.check(context)
            if not isinstance(cft, (CategoryType, DocumentType)):
                raise SyntaxError("Cannot copy from " + cft.getName())
        if self.assignments is not None:
            for assignment in self.assignments:
                if not cd.hasAttribute(context, assignment.getName()):
                    raise SyntaxError("\"" + assignment.getName() +
                        "\" is not an attribute of " + self.itype.typeName)
                assignment.check(context)
        return itype

    def interpret(self, context:Context):
        instance = self.itype.newInstance(context)
        instance.mutable = True
        if self.copyFrom is not None:
            copyObj = self.copyFrom.interpret(context)
            from prompto.declaration.CategoryDeclaration import CategoryDeclaration
            cd = context.getRegisteredDeclaration(CategoryDeclaration, self.itype.typeName)
            if isinstance(copyObj, IInstance):
                for name in copyObj.getMemberNames():
                    if cd.hasAttribute(context, name):
                        value = copyObj.getMemberValue(context, name)
                        if value is not None and value.mutable and not self.itype.mutable:
                            raise NotMutableError()
                        instance.setMember(context, name, value)
            elif isinstance(copyObj, Document):
                for name in copyObj.getMemberNames():
                    if cd.hasAttribute(context, name):
                        value = copyObj.getMemberValue(context, name)
                        if value is not None and value.mutable and not self.itype.mutable:
                            raise NotMutableError()
                        # TODO convert to attribute type
                        instance.setMember(context, name, value)
        if self.assignments is not None:
            for assignment in self.assignments:
                value = assignment.getExpression().interpret(context)
                if value is not None and value.mutable and not self.itype.mutable:
                    raise NotMutableError()
                instance.setMember(context, assignment.getName(), value)
        instance.mutable = self.itype.mutable
        return instance
