from presto.grammar.BaseArgument import BaseArgument
from presto.grammar.INamedValue import INamedValue
from presto.grammar.ITypedArgument import ITypedArgument
from presto.type.CodeType import CodeType


class CodeArgument ( BaseArgument, ITypedArgument ):

    def __init__(self, name):
        super(CodeArgument, self).__init__(name)

    def getType(self, context=None):
        return CodeType.instance

    def getSignature(self, dialect):
        return self.name + ':' + CodeType.instance.getName()

    def getProto(self, context):
        return CodeType.instance.getName()

    def __str__(self):
        return self.name + ':' + CodeType.instance.getName()

    def toDialect(self, writer):
        writer.append(CodeType.instance.getName())
        writer.append(" ")
        writer.append(self.name)

    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, CodeArgument):
            return False
        return self.name==obj.name

    def register(self, context):
        actual = context.getRegisteredValue(INamedValue, self.name)
        if actual is not None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        context.registerValue(self)

    def check(self, context):
        pass
