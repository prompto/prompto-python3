from prompto.statement.BaseStatement import BaseStatement
from prompto.type.TypeMap import TypeMap
from prompto.type.VoidType import VoidType


class BaseSwitchStatement(BaseStatement):

    def __init__(self):
        super(BaseSwitchStatement, self).__init__()
        self.switchCases = []
        self.defaultCase = None

    def setSwitchCases(self, switchCases):
        self.switchCases = switchCases

    def addSwitchCase(self, switchCase):
        self.switchCases.append(switchCase)

    def setDefaultCase(self, defaultCase):
        self.defaultCase = defaultCase

    def check(self, context):
        self.checkSwitchCasesType(context)
        return self.checkReturnType(context)

    def checkSwitchCasesType(self, context):
        itype = self.checkSwitchType(context)
        if self.switchCases is not None:
            for sc in self.switchCases:
                sc.checkSwitchType(context, itype)

    def checkReturnType(self, context):
        types = TypeMap()
        self.collectReturnTypes(context, types)
        return types.inferType(context)

    def collectReturnTypes(self, context, types):
        if self.switchCases is not None:
            for sc in self.switchCases:
                itype = sc.checkReturnType(context)
                if itype != VoidType.instance:
                    types[itype.getName()] = itype
        if self.defaultCase is not None:
            itype = self.defaultCase.check(context, None)
            if itype != VoidType.instance:
                types.put(itype.getName(), itype)

    def interpretSwitch(self, context, switchValue, toThrow):
        if self.switchCases is not None:
            for sc in self.switchCases:
                if sc.matches(context, switchValue):
                    return sc.interpret(context)
        if self.defaultCase is not None:
            return self.defaultCase.interpret(context)
        if toThrow is not None:
            raise toThrow
        return None

    def canReturn(self):
        return True