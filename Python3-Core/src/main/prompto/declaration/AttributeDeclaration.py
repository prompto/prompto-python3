from prompto.declaration.BaseDeclaration import BaseDeclaration
from prompto.error.InternalError import InternalError
from prompto.expression.IExpression import IExpression
from prompto.value.IValue import IValue


class AttributeDeclaration ( BaseDeclaration ):

    def __init__(self, name, type_, constraint=None):
        super(AttributeDeclaration, self).__init__(name)
        self.type_ = type_
        self.constraint = constraint
        self.storable = False

    def getType(self, context = None):
        return self.type_

    def getConstraint(self):
        return self.constraint

    def __str__(self):
        return self.getName() + ':' + str(self.type_)

    def toEDialect(self, writer):
            writer.append("define ")
            writer.append(self.getName())
            writer.append(" as ")
            if self.storable:
                writer.append(" storable")
            self.type_.toDialect(writer)
            writer.append(" attribute")
            if self.constraint is not None:
                self.constraint.toDialect(writer)

    def toODialect(self, writer):
            if self.storable:
                writer.append("storable ")
            writer.append("attribute ")
            writer.append(self.getName())
            writer.append(" : ")
            self.type_.toDialect(writer)
            if self.constraint is not None:
                self.constraint.toDialect(writer)
            writer.append(';')

    def toSDialect(self, writer):
            if self.storable:
                writer.append("storable ")
            writer.append("attr ")
            writer.append(self.getName())
            writer.append(" ( ")
            self.type_.toDialect(writer)
            writer.append(" ):\n")
            writer.indent()
            if self.constraint is not None:
                self.constraint.toDialect(writer)
            else:
                writer.append("pass")
            writer.dedent()

    def register(self, context):
        context.registerDeclaration(self)

    def check(self, context):
        self.type_.checkExists(context)
        return self.type_

    def setConstraint(self, constraint):
        self.constraint = constraint

    def checkValue(self, context, value):
        if isinstance(value, IExpression):
            value = value.interpret(context)
        if self.constraint is None:
            return value
        self.constraint.checkValue(context, value)
        return value
