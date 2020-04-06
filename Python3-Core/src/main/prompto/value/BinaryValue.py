from prompto.intrinsic.Binary import Binary
from prompto.value.BaseValue import BaseValue


class BinaryValue(BaseValue):

    def __init__(self, itype, binary=None, mimeType=None, data=None):
        super().__init__(itype)
        if mimeType is not None and data is not None:
            binary = Binary(mimeType, data)
        self.binary = binary


    def __getattr__(self, item):
        return getattr(self.binary, item, None)
