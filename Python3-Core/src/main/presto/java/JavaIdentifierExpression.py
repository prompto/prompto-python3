from presto.java.JavaExpression import JavaExpression

class JavaIdentifierExpression (JavaExpression):

    @staticmethod
    def parse(ids):
        parts = ids.split("\\.")
        result = None
        for part in parts:
            result = JavaIdentifierExpression(parent=result, identifier=part)
        return result

    def __init__(self, identifier, parent = None, isChildClass = False):
        self.parent = parent
        self.identifier = identifier
        self.isChildClass = isChildClass

    def getParent(self):
        return self.parent

    def getIdentifier(self):
        return self.identifier

    def __str__(self):
        if self.parent is None:
            return self.identifier
        else:
            return str(self.parent) + ('$' if self.isChildClass else '.') + self.identifier

    def toDialect(self, writer):
        if self.parent is not None:
            self.parent.toDialect(writer)
            if self.isChildClass:
                writer.append("$")
            else:
                writer.append(".")
        writer.append(self.identifier)
