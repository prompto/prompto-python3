import sys
import importlib

class PythonModule(object):

    def __init__(self, ids:list):
        self.ids = ids

    def __str__(self):
        return ".".join(self.ids)

    def resolve(self):
        fullName = str(self)
        m = sys.modules.get(fullName, None)
        if m is not None:
            return m
        try:
            return importlib.import_module(fullName)
        except Exception as e:
            return None

    def toDialect(self, writer):
        writer.append(" from module: ")
        for id_ in self.ids:
            writer.append(id_)
            writer.append('.')
        writer.trimLast(1)
