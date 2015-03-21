from presto.literal.Literal import Literal
from presto.value.SetValue import SetValue
from presto.type.MissingType import MissingType
from presto.type.SetType import SetType

class SetLiteral(Literal):

    def __init__(self, expressions = []):
        strs = [ str(e) for e in expressions]
        super().__init__("<" + ", ".join(strs) + ">", SetValue(MissingType.instance))
        self.expressions = expressions
        self.itemType = None

    def check(self, context):
        if self.itemType is None:
            self.itemType = self.inferElementType(context)
        return SetType(self.itemType)

    def inferElementType(self, context):
        if len(self.expressions)==0:
            return MissingType.instance
        lastType = None
        for e in self.expressions:
            elemType = e.check(context)
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
        if len(self.value)==0 and len(self.expressions)>0:
            self.check(context) # force computation of itemType
            xvalue = set()
            for exp in self.expressions:
                xvalue.add(exp.interpret(context))
            self.value = SetValue(self.itemType, xvalue)
        return self.value

    def toDialect(self, writer):
        writer.append('<')
        if len(self.expressions)>0:
            for item in self.expressions:
                item.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)
        writer.append('>')
