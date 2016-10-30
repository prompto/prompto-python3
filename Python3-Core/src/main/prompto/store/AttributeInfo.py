
class AttributeInfo(object):

    def __init__(self, name, family, collection, indexTypes):
        self.name = name
        self.family = family
        self.collection = collection
        self.key = "key" in indexTypes if indexTypes is not None else False
        self.value = "value" in indexTypes if indexTypes is not None else False
        self.words = "words" in indexTypes if indexTypes is not None else False

