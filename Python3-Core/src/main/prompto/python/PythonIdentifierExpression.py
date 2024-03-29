from prompto.python.PythonExpression import PythonExpression
from types import ModuleType

from prompto.store.DataStore import DataStore


class PythonIdentifierExpression(PythonExpression):

    @staticmethod
    def parse(ids):
        parts = ids.split("\\.")
        result = None
        for part in parts:
            result = PythonIdentifierExpression(parent=result, name=part)
        return result


    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name


    def getParent(self):
        return self.parent


    def getIdentifier(self):
        return self.name


    def __str__(self):
        if self.parent == None:
            return self.name
        else:
            return str(self.parent) + '.' + self.name


    def toDialect(self, writer):
        if self.parent is not None:
            self.parent.toDialect(writer)
            writer.append(".")
        writer.append(self.name)


    def interpret(self, context, module):
        if self.parent is None:
            return self.interpret_root(context, module)
        else:
            return self.interpret_child(context, module)


    def interpret_root(self, context, module):
        o = self.interpret_prompto(context)
        if o is not None:
            return o
        o = self.interpret_global()
        if o is not None:
            return o
        o = self.interpret_instance(context)
        if o is not None:
            return o
        o = self.interpret_module(module)
        if o is not None:
            return o
        return None


    def interpret_prompto(self, context):
        if self.name== "$context":
            return context
        elif self.name == "$store":
            return DataStore.instance
        else:
            return None


    def interpret_global(self):
        try:
            return eval(self.name)
        except:
            return None


    def interpret_module(self, module):
        if module is None:
            return None
        else:
            try:
                m = module.resolve()
                o = m.__dict__.get(self.name, None)
                if o is None:
                    return m
                else:
                    return o
            except:
                return None


    def interpret_instance(self, context):
        if self.name == "None":
            return None
        else:
            try:
                return context.getValue(self.name)
            except:
                return None


    def interpret_child(self, context, module):
        o = self.parent.interpret(context, module)
        if o is not None:
            o = self.interpret_field(o)
        return o

    def interpret_field(self, o):
        if isinstance(o, ModuleType):
            o = o.__dict__
        return o.get(self.name, None)
