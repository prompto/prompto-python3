from presto.declaration.CategoryDeclaration import CategoryDeclaration
from presto.declaration.IDeclaration import IDeclaration
from presto.expression.ConstructorExpression import ConstructorExpression
from presto.expression.IExpression import IExpression
from presto.expression.MethodSelector import MethodSelector
from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from presto.grammar.UnresolvedIdentifier import UnresolvedIdentifier
from presto.parser.Dialect import Dialect
from presto.runtime.Context import Context
from presto.statement.BaseStatement import BaseStatement
from presto.statement.MethodCall import MethodCall
from presto.statement.SimpleStatement import SimpleStatement
from presto.type.CategoryType import CategoryType
from presto.error.SyntaxError import SyntaxError
from presto.utils.CodeWriter import CodeWriter

class UnresolvedCall(SimpleStatement):

    def __init__(self, caller:IExpression, assignments:ArgumentAssignmentList):
        self.resolved = None
        self.caller = caller
        self.assignments = assignments

    def getCaller(self):
        return self.caller

    def getAssignments(self):
        return self.assignments

    def toDialect(self, writer):
        try:
            self.resolve(writer.context)
            self.resolved.toDialect(writer)
        except:
            self.caller.toDialect(writer)
            if self.assignments is not None:
                self.assignments.toDialect(writer)

    def check(self, context:Context):
        return self.resolveAndCheck(context)

    def interpret(self, context:Context):
        if self.resolved is None:
            self.resolveAndCheck(context)
        return self.resolved.interpret(context)

    def resolveAndCheck(self, context:Context):
        self.resolve(context)
        return self.resolved.check(context)

    def resolve(self, context:Context):
        if self.resolved is None:
            if isinstance(self.caller, UnresolvedIdentifier):
                self.resolved = self.resolveUnresolvedIdentifier(context)
            else:
                self.resolved = self.resolveMember(context)
        return self.resolved

    def resolveUnresolvedIdentifier(self, context:Context):
        name = self.caller.getName()
        decl = context.getRegisteredDeclaration(IDeclaration, name)
        if decl is None:
            raise SyntaxError("Unknown name:" + name)
        if isinstance(decl, CategoryDeclaration):
            return ConstructorExpression(CategoryType(name), self.assignments)
        else:
            return MethodCall(MethodSelector(name), self.assignments)

    def resolveMember(self, context:Context):
        parent = self.caller.getParent()
        name = self.caller.getName()
        return MethodCall(MethodSelector(name, parent), self.assignments)

    def interpretAssert(self, context, testMethodDeclaration):
        self.resolve(context)
        if getattr(self.resolved, "interpretAssert", None) is not None:
            return self.resolved.interpretAssert(context, testMethodDeclaration)
        else:
            writer = CodeWriter(self.dialect, context)
            self.resolved.toDialect(writer)
            raise SyntaxError("Cannot test '" + str(writer) + "'")
