from prompto.runtime.Variable import Variable
from prompto.type.IType import IType


class WidgetField(Variable):

    def __init__(self, name: str, itype: IType):
        super().__init__(name, itype)