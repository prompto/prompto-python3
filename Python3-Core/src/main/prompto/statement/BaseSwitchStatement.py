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
        type_ = self.checkSwitchType(context)
        if self.switchCases is not None:
            for sc in self.switchCases:
                sc.checkSwitchType(context, type_)

    def checkReturnType(self, context):
        types = TypeMap()
        self.collectReturnTypes(context, types)
        return types.inferType(context)

    def collectReturnTypes(self, context, types):
        if self.switchCases is not None:
            for sc in self.switchCases:
                type_ = sc.checkReturnType(context)
                if type_ != VoidType.instance:
                    types[type_.getName()] = type_
        if self.defaultCase is not None:
            type_ = self.defaultCase.check(context, None)
            if type_ != VoidType.instance:
                types.put(type_.getName(), type_)

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