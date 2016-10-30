from prompto.type.BinaryType import BinaryType


class ImageType(BinaryType):

    instance = None

    def __init__(self):
        super(ImageType, self).__init__(TypeFamily.IMAGE)

ImageType.instance = ImageType()