from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.declaration.ClosureDeclaration import ClosureDeclaration
from prompto.runtime.Variable import Variable
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.MethodType import MethodType
from prompto.type.VoidType import VoidType
from prompto.value.ClosureValue import ClosureValue
from prompto.value.ExpressionValue import ExpressionValue
from prompto.error.SyntaxError import SyntaxError


class DeclarationInstruction(BaseStatement):

    def __init__(self, declaration):
        super(DeclarationInstruction, self).__init__()
        self.declaration = declaration

    def getDeclaration(self):
        return self.declaration

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
            typ = MethodType(context, method.getName())
            context.registerValue( Variable(method.getName(), typ))
            context.setValue(method.getName(), ClosureValue(context, method))
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
