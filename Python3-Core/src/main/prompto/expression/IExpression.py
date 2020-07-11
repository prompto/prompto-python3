from prompto.grammar.IDialectElement import IDialectElement


class IExpression(IDialectElement):

    def interpret(self, context):
        raise Exception("You must override interpret in " + type(self).__name__)


    def checkAttribute(self, context):
        raise SyntaxError("Expected an attribute, got: " + str(self))


