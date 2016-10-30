from prompto.constraint.IAttributeConstraint import IAttributeConstraint
from prompto.store.InvalidValueError import InvalidValueError
from prompto.runtime.TransientVariable import TransientVariable
from prompto.type.AnyType import AnyType
from prompto.value.Boolean import Boolean


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
            raise InvalidValueError(str(value) + " does not match:" + str(self.expression))

    def toDialect(self, writer):
        writer.append(" matching ")
        self.expression.toDialect(writer)
