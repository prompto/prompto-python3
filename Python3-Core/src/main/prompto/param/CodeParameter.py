from prompto.param.BaseParameter import BaseParameter
from prompto.param.ITypedParameter import ITypedParameter
from prompto.grammar.INamedInstance import INamedInstance
from prompto.type.CodeType import CodeType
from prompto.error.SyntaxError import SyntaxError

class CodeParameter (BaseParameter, ITypedParameter):

    def __init__(self, name):
        super(CodeParameter, self).__init__(name)

    def getType(self, context=None):
        return CodeType.instance

    def getSignature(self, dialect):
        return self.name + ':' + CodeType.instance.typeName

    def getProto(self):
        return CodeType.instance.typeName

    def __str__(self):
        return self.name + ':' + CodeType.instance.typeName

    def toDialect(self, writer):
        writer.append(CodeType.instance.typeName)
        writer.append(" ")
        writer.append(self.name)

    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, CodeParameter):
            return False
        return self.name==obj.name

    def register(self, context):
        actual = context.getRegisteredValue(INamedInstance, self.name)
        if actual is not None:
            raise SyntaxError("Duplicate argument: \"" + self.name + "\"")
        context.registerValue(self)

    def check(self, context):
        pass
