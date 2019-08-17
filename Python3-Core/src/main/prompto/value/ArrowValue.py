from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.expression.ArrowExpression import ArrowExpression
from prompto.runtime.Context import Context
from prompto.value.ContextualExpression import ContextualExpression


class ArrowValue(ContextualExpression):

    def __init__(self, method: IMethodDeclaration, calling: Context, arrow: ArrowExpression):
        super().__init__(calling, arrow)
        self.method = method

    def interpret(self, context: Context):
        parent = context.getParentContext()
        try:
            context.setParentContext(self.calling)
            return self.expression.interpret(context)
        except:
            context.setParentContext(parent)
