from prompto.expression.ValueExpression import ValueExpression
from prompto.grammar.ArgumentAssignment import ArgumentAssignment
from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from prompto.literal.TextLiteral import TextLiteral
from prompto.type.IType import IType
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


    def isAssignableFrom(self, context, other:IType):
        from prompto.type.CategoryType import CategoryType
        return super().isAssignableFrom(context, other) or \
            other is AnyType.instance or \
            (isinstance(other, CategoryType) and "Any"==other.typeName)


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


    def withItemType(self, itemType:IType):
        return self


    def sort(self, context, source, desc, key):
        if key is None:
            key = TextLiteral('"key"')
        if self.globalMethodExists(context, str(key)):
            return self.sortByGlobalMethod(context, source, desc, str(key))
        elif isinstance(key, TextLiteral):
            return self.sortByEntry(context, source, desc, key.getValue().getStorableData())
        else:
            return self.sortByExpression(context, source, desc, key)


    def globalMethodExists(self, context, name):
        from prompto.runtime.Context import MethodDeclarationMap
        methods = context.getRegisteredDeclaration(MethodDeclarationMap, name)
        if methods is None:
            return False
        else:
            return methods.get(self.typeName, None)


    def sortByGlobalMethod(self, context, source, desc, name):
        from prompto.statement.MethodCall import MethodCall
        from prompto.value.Document import Document
        exp = ValueExpression(self, Document())
        arg = ArgumentAssignment(None, exp)
        args = ArgumentAssignmentList(items=[arg])
        from prompto.expression.MethodSelector import MethodSelector
        call = MethodCall(MethodSelector(name), args)
        return self.doSortByGlobalMethod(context, source, desc, call)


    def doSortByGlobalMethod(self, context, source, desc, call):

        def keyGetter(o):
            assignment = call.assignments[0]
            assignment.setExpression(ValueExpression(self, o))
            return call.interpret(context)

        return sorted(source, key=keyGetter, reverse=desc)


    def sortByEntry(self, context, source, desc, name):

        def keyGetter(o):
            return o.getMemberValue(context, name)

        return sorted(source, key=keyGetter, reverse=desc)

    def sortByExpression(self, context, source, desc, exp):

        def keyGetter(o):
            co = context.newDocumentContext(o, False)
            return exp.interpret(co)

        return sorted(source, key=keyGetter, reverse=desc)


DocumentType.instance = DocumentType()

