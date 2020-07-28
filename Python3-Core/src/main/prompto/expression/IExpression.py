from prompto.grammar.IDialectElement import IDialectElement
from prompto.error.SyntaxError import SyntaxError


class IExpression(IDialectElement):

    def check(self, context):
        raise Exception("You must override check in " + type(self).__name__)


    def checkReference(self, context):
        return self.check(context)


    def interpret(self, context):
        raise Exception("You must override interpret in " + type(self).__name__)


    def interpretReference(self, context):
        return self.interpret(context)


    def checkAttribute(self, context):
        raise SyntaxError("Expected an attribute, got: " + str(self))


