from prompto.type.BinaryType import BinaryType


class BlobType(BinaryType):

    instance = None

    def __init__(self):
        super(BlobType, self).__init__("Blob")

BlobType.instance = BlobType()