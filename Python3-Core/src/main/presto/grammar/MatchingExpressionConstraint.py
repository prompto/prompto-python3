from presto.error.InvalidDataError import InvalidDataError
from presto.grammar.IAttributeConstraint import IAttributeConstraint
from presto.runtime.TransientVariable import TransientVariable
from presto.type.AnyType import AnyType
from presto.value.Boolean import Boolean


class MatchingExpressionConstraint ( IAttributeConstraint ) :

    def __init__(self, expression):
        super(MatchingExpressionConstraint, self).__init__()
        self.expression = expression

    def checkValue(self, context, value):
        child = context.newChildContext()
        child.registerValue(TransientVariable("value", AnyType.instance))
        child.setValue("value", value)
        test = self.expression.interpret(child)
        if not Boolean.TRUE==test:
            raise InvalidDataError(str(value) + " does not match:" + str(self.expression))

    def toDialect(self, writer):
        writer.append(" matching ")
        self.expression.toDialect(writer)
