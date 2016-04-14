from prompto.expression.IExpression import IExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier

class SelectorExpression (IExpression):

    def __init__(self, parent = None):
        self.parent = parent

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def checkParent(self, context):
        if isinstance(self.parent, UnresolvedIdentifier):
            return self.parent.checkMember(context)
        else:
            return self.parent.check(context)
