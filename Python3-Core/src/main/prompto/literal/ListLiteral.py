from prompto.expression.IExpression import IExpression
from prompto.literal.Literal import Literal
from prompto.type.CharacterType import CharacterType
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.type.ListType import ListType
from prompto.type.MissingType import MissingType
from prompto.type.TextType import TextType
from prompto.value.Decimal import Decimal
from prompto.value.ListValue import ListValue
from prompto.error.SyntaxError import SyntaxError
from prompto.value.Text import Text


class ListLiteral(Literal):

    def __init__(self, expressions=[]):
        strs = [ str(e) for e in expressions]
        super().__init__("[" + ", ".join(strs) + "]", ListValue(MissingType.instance))
        self.itemType = None
        self.expressions = expressions

    def check(self, context):
        if self.itemType == None:
            self.itemType = self.inferElementType(context)
        return ListType(self.itemType)

    def inferElementType(self, context):
        if len(self.expressions)==0:
            return MissingType.instance
        lastType = None
        for o in self.expressions:
            elemType = o.check(context)
            if lastType == None:
                lastType = elemType
            elif lastType != elemType:
                if elemType.isAssignableTo(context, lastType):
                    pass  # lastType is less specific
                elif lastType.isAssignableTo(context, elemType):
                    lastType = elemType  # elemType is less specific
                else:
                    raise SyntaxError("Incompatible types: " + str(elemType) + " and " + str(lastType))
        return lastType

    def interpret(self, context):
        if self.value.isEmpty() and len(self.expressions)>0:
            self.check(context) # force computation of item type
            value = ListValue(self.itemType)
            for o in self.expressions:
                o = o.interpret(context)
                o = self.interpretPromotion(o)
                value.items.append(o)
            self.value = value
        return self.value


    def interpretPromotion(self, item):
        if item is None:
            return item
        if DecimalType.instance == self.itemType and item.type == IntegerType.instance:
            return Decimal(item.DecimalValue())
        elif TextType.instance == self.itemType and item.type == CharacterType.instance:
            return Text(item.value)
        else:
            return item

    def toDialect(self, writer):
        writer.append('[')
        if len(self.expressions)>0:
            for item in self.expressions:
                item.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)
        writer.append(']')

