from prompto.grammar.IDialectElement import IDialectElement


class IExpression(IDialectElement):

    def interpret(self, context):
        raise Exception("You must override interpret in " + type(self).__name__)