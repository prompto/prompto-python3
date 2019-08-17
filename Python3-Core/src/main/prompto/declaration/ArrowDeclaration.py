# a dummy declaration to interpret arrow expressions in context
from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.value.ArrowValue import ArrowValue


class ArrowDeclaration(AbstractMethodDeclaration):

    def __init__(self, arrow: ArrowValue):
        super().__init__("%Arrow", arrow.method.parameters, arrow.method.returnType)
        self.arrow = arrow

    def interpret(self, context):
        return self.arrow.interpret(context)
