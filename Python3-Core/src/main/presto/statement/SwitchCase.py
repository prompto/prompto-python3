from presto.parser.ISection import ISection
from presto.parser.Section import Section


class SwitchCase ( Section, ISection ):

    def __init__(self, expression, statements):
        super().__init__()
        self.expression = expression
        self.statements = statements

    def checkReturnType(self, context):
        return self.statements.check(context)

    def interpret(self, context):
        return self.statements.interpret(context)


class SwitchCaseList(list):

    def __init__(self, item:SwitchCase=None):
        super().__init__()
        if item is not None:
            self.append(item)
