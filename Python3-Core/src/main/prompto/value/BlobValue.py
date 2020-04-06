from prompto.type.BlobType import BlobType
from prompto.value.BinaryValue import BinaryValue


class BlobValue(BinaryValue):

    def __init__(self, binary=None, mimeType=None, data=None):
        super().__init__(BlobType.instance, binary=binary, mimeType=mimeType, data=data)

