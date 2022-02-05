from prompto.declaration.BaseMethodDeclaration import BaseMethodDeclaration
from prompto.type.VoidType import VoidType
from prompto.error.SyntaxError import SyntaxError

class AbstractMethodDeclaration(BaseMethodDeclaration):

    def __init__(self, name, arguments, returnType):
        super(AbstractMethodDeclaration, self).__init__(name, arguments)
        self.returnType = returnType if returnType is not None else VoidType.instance


    def checkMember(self, category, context):
        pass  # TODO


    def checkStart(self, context):
        if self.parameters is not None:
            self.parameters.check(context)
        local = context.newLocalContext()
        self.registerParameters(local)
        return self.returnType


    def check(self, context):
        if self.parameters is not None:
            self.parameters.check(context)
        return self.returnType


    def checkChild(self, context):
        if self.parameters is not None:
            self.parameters.check(context)
        return self.returnType


    def interpret(self, context):
        raise SyntaxError("Should never get there !")


    def toMDialect(self, writer):
        writer.append("abstract def ")
        writer.append(self.name)
        writer.append(" (")
        self.parameters.toDialect(writer)
        writer.append(")")
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("->")
            self.returnType.toDialect(writer)


    def toODialect(self, writer):
        writer.append("abstract ")
        if self.returnType is not None and self.returnType is not VoidType.instance:
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("method ")
        writer.append(self.name)
        writer.append(" (")
        self.parameters.toDialect(writer)
        writer.append(");")


    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as abstract method ")
        self.parameters.toDialect(writer)
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("returning ")
            self.returnType.toDialect(writer)

    def isAbstract(self):
        return True
