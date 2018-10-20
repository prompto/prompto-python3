from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.runtime.Variable import Variable
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.MethodType import MethodType
from prompto.type.VoidType import VoidType
from prompto.value.ClosureValue import ClosureValue
from prompto.error.SyntaxError import SyntaxError


class DeclarationStatement(BaseStatement):

    def __init__(self, declaration):
        super(DeclarationStatement, self).__init__()
        self.declaration = declaration
        if isinstance(declaration, IMethodDeclaration):
            declaration.declarationOf = self


    def __str__(self):
        # TODO Auto-generated method stub
        return self.declaration.toString()


    def check(self, context):
        if isinstance(self.declaration, ConcreteMethodDeclaration):
            self.declaration.checkChild(context)
            self.declaration.register(context)
        else:
            raise SyntaxError("Unsupported:" + type(self.declaration).__name__)
        return VoidType.instance


    def interpret(self, context):
        if isinstance(self.declaration, ConcreteMethodDeclaration):
            method = self.declaration
            method.register(context)
            typ = MethodType(method)
            context.registerValue( Variable(method.getName(), typ))
            context.setValue(method.getName(), ClosureValue(context, typ))
            return None
        else:
            raise SyntaxError("Unsupported:" + type(self.declaration).__name__)


    def toDialect(self, writer):
        if isinstance(self.declaration, ConcreteMethodDeclaration):
            try:
                writer.context.registerMethodDeclaration(self.declaration)
            except:
                pass # ok
        self.declaration.toDialect(writer)
