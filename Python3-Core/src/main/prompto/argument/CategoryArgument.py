from prompto.argument.BaseArgument import BaseArgument
from prompto.argument.ITypedArgument import ITypedArgument


class CategoryArgument(BaseArgument, ITypedArgument):

    def __init__(self, type_, name):
        super(CategoryArgument, self).__init__(name)
        self.type_ = type_

    def getSignature(self, dialect):
        return self.getProto()

    def getProto(self, context):
        return self.type_.getName()

    def __str__(self):
        return self.name + ':' + self.getProto()

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj == None:
            return False
        if not isinstance(obj, CategoryArgument):
            return False
        return self.getType() == obj.getType() \
            and self.getName() == obj.getName()

    def register(self, context):
        from prompto.grammar.INamedValue import INamedValue
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual != None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        context.registerValue(self)
        if self.defaultExpression is not None:
            context.setValue(self.name, self.defaultExpression)

    def check(self, context):
        self.type_.checkExists(context)

    def getType(self, context=None):
        return self.type_

    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        super(CategoryArgument, self).toDialect(writer)
        if self.defaultExpression is not None:
            writer.append(" = ")
            self.defaultExpression.toDialect(writer)


    def toEDialect(self, writer):
        anonymous = "any"==self.type_.name
        self.type_.toDialect(writer)
        if anonymous:
            writer.append(' ')
            writer.append(self.name)
        if not anonymous:
            writer.append(' ')
            writer.append(self.name)


    def toODialect(self, writer):
        self.type_.toDialect(writer)
        writer.append(' ')
        writer.append(self.name)

    def toSDialect(self, writer):
        writer.append(self.name)
        writer.append(':')
        self.type_.toDialect(writer)
