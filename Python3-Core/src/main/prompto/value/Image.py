from prompto.type.ImageType import ImageType
from prompto.value.BinaryValue import BinaryValue


class Image(BinaryValue):

    def __init__(self, mimeType, data):
        super().__init__(ImageType.instance, mimeType, data)

