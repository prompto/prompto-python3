from prompto.declaration.ConcreteMethodDeclaration import *
from prompto.value.NullValue import NullValue


class NativeMethodDeclaration(ConcreteMethodDeclaration):

    def __init__(self, name, arguments, returnType, statements):
        super().__init__(name, arguments, returnType, statements)

    def interpret(self, context):
        context.enterMethod(self)
        try:
            result = self.statements.interpretNative(context, self.returnType)
            return self.castToReturnType(context, result)
        finally:
            context.leaveMethod(self)

    def castToReturnType(self, context, value):
        if value is None:
            return NullValue.instance
        # can only cast to specified type, and if required
        if self.returnType is not None and value is not None and not self.returnType.isAssignableFrom(context, value.itype):
            # only cast if implemented, on a per type basis
            if hasattr(self.returnType, "nativeCast"):
                value = self.returnType.nativeCast(context, value)
        return value


    def checkStatements(self, context, returnType: IType):
        return self.statements.checkNative(context, returnType)


    def toMDialect(self, writer):
        writer.append("def ")
        if self.memberOf is None:
            writer.append("native ")
        writer.append(self.name)
        writer.append(" (")
        self.parameters.toDialect(writer)
        writer.append(")")
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("->")
            self.returnType.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()


    def toODialect(self, writer):
        if self.returnType is not None and self.returnType is not VoidType.instance:
            self.returnType.toDialect(writer)
            writer.append(" ")
        if self.memberOf is None:
            writer.append("native ")
        writer.append("method ")
        writer.append(self.name)
        writer.append(" (")
        self.parameters.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        for stmt in self.statements:
            stmt.toDialect(writer)
            writer.newLine()
        writer.dedent()
        writer.append("}\n")


    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as ")
        if self.memberOf is None:
            writer.append("native ")
        writer.append("method ")
        self.parameters.toDialect(writer)
        if self.returnType is not None and self.returnType is not VoidType.instance:
            writer.append("returning ")
            self.returnType.toDialect(writer)
            writer.append(" ")
        writer.append("doing:\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("\n")
