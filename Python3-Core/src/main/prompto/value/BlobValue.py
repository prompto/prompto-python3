from prompto.type.BlobType import BlobType
from prompto.value.BinaryValue import BinaryValue


class BlobValue(BinaryValue):

    def __init__(self, mimeType, data):
        super().__init__(BlobType.instance, mimeType, data)

