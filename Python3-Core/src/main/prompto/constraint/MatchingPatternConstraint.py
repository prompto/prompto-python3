import re

from prompto.constraint.IAttributeConstraint import *
from prompto.store.InvalidValueError import *


class MatchingPatternConstraint ( IAttributeConstraint ) :

    def __init__(self, expression):
        super(MatchingPatternConstraint, self).__init__()
        self.expression = expression
        self.pattern = None

    def checkValue(self, context, value):
        if self.pattern is None:
            toMatch = self.expression.interpret(context)
            self.pattern = re.compile(str(toMatch))
        if not re.match(self.pattern,str(value)):
            raise InvalidValueError(str(value) + " does not match:" + str(self.pattern))

    def toDialect(self, writer):
        writer.append(" matching ")
        self.expression.toDialect(writer)
