from prompto.declaration.BaseMethodDeclaration import BaseMethodDeclaration
from prompto.error.InternalError import InternalError
from prompto.grammar.ArgumentList import ArgumentList



class BuiltInMethodDeclaration(BaseMethodDeclaration):

    def __init__(self, name, *args):
        argsList = None if len(args) == 0 else ArgumentList(*args)
        super().__init__(name, argsList)


    def getValue(self, context):
        from prompto.runtime.Context import BuiltInContext
        while context is not None:
            if isinstance(context, BuiltInContext):
                return context.value
            context = context.getParentContext()
        raise InternalError("Could not locate context for built-in value!")
