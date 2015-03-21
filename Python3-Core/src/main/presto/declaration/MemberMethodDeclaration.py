from presto.declaration.ConcreteMethodDeclaration import *
from presto.declaration.ICategoryMethodDeclaration import *
from presto.expression.IExpression import *


class MemberMethodDeclaration ( ConcreteMethodDeclaration, IExpression, ICategoryMethodDeclaration ):

    def __init__(self, name, arguments, returnType, instructions):
        super(MemberMethodDeclaration, self).__init__(name, arguments,returnType, instructions)

    def checkMember(self, category, context):
        pass  # TODO
