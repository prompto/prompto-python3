from prompto.type.MissingType import MissingType
from prompto.type.NullType import NullType
from prompto.type.TextType import TextType
from prompto.type.AnyType import AnyType
from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily
from prompto.value.NullValue import NullValue
from prompto.value.Boolean import Boolean
from prompto.value.Decimal import Decimal
from prompto.value.Integer import Integer
from prompto.value.Text import Text


class DocumentType ( NativeType ):

    instance = None

    def __init__(self):
        super(DocumentType, self).__init__(TypeFamily.DOCUMENT)


    def checkMember(self, context, name):
        return AnyType.instance


    def checkItem(self, context, itemType):
        if itemType is TextType.instance:
            return AnyType.instance
        else:
            raise Exception("text") # TODO


    def isMoreSpecificThan(self, context, other):
        if isinstance(other, (NullType, AnyType, MissingType)):
            return True
        else:
            return super().isMoreSpecificThan(context, other)



    def readJSONValue(self, context, node, parts):
        from prompto.value.Document import Document
        instance = Document()
        for key, node in node.items():
            value = self.readJSONField(context, node, parts)
            instance.setMember(context, key, value)
        return instance

    def readJSONField(self, context, node, parts):
        if node is None:
            return NullValue.instance
        elif isinstance(node, bool):
            return Boolean.ValueOf(node)
        elif isinstance(node, int):
            return Integer(node)
        elif isinstance(node, float):
            return Decimal(node)
        elif isinstance(node, str):
            return Text(node)
        elif isinstance(node, list):
            raise Exception("list")
        elif isinstance(node, dict):
            raise Exception("dict")
        elif isinstance(node, object):
            raise Exception("object")
        else:
            raise Exception(str(type(node)))

DocumentType.instance = DocumentType()

