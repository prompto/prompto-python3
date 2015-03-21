from presto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from presto.declaration.ClosureDeclaration import ClosureDeclaration
from presto.runtime.Variable import Variable
from presto.statement.BaseStatement import BaseStatement
from presto.type.MethodType import MethodType
from presto.type.VoidType import VoidType
from presto.value.ClosureValue import ClosureValue
from presto.value.ExpressionValue import ExpressionValue


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
                writer.context.registerMethod(self.declaration)
            except:
                pass # ok
        self.declaration.toDialect(writer)
