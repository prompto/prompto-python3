from prompto.declaration.GetterMethodDeclaration import GetterMethodDeclaration

class NativeGetterMethodDeclaration(GetterMethodDeclaration):

    def __init__(self, name, statements):
        super().__init__(name, statements)

    def interpret(self, context):
        context.enterMethod(self)
        try:
            result = self.statements.interpretNative(context, self.returnType)
            return self.castToReturnType(context, result)
        finally:
            context.leaveMethod(self)

    def castToReturnType(self, context, value):
        # can only cast to specified type, and if required
        if self.returnType is not None and value is not None and not value.type.isAssignableTo(context, self.returnType):
            # only cast if implemented, on a per type basis
            if self.returnType.nativeCast:
                value = self.returnType.nativeCast(context, value)
        return value
