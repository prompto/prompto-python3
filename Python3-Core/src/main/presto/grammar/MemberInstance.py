from presto.error.InvalidDataError import InvalidDataError
from presto.grammar.IAssignableInstance import IAssignableInstance
from presto.value.Document import Document


class MemberInstance ( IAssignableInstance ):

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def setParent(self, parent):
        self.parent = parent

    def getName(self):
        return self.name

    def __str__(self):
        return str(self.parent) + "." + self.name

    def toDialect(self, writer):
        self.parent.toDialect(writer)
        writer.append(".")
        writer.append(self.name)

    def checkAssignValue(self, context, expression):
        self.parent.checkAssignMember(context, self.name)
        expression.check(context)

    def checkAssignMember(self, context, memberName):
        self.parent.checkAssignMember(context, self.name)

    def checkAssignElement(self, context):
        pass

    def assign(self, context, expression):
        value = expression.interpret(context)
        doc = self.parent.interpret(context)
        if isinstance(doc, Document):
            doc.setMember(self.name,value)
        else:
            raise InvalidDataError("Expecting a document, got:" + type(doc).__name__)

    def interpret(self, context):
        doc = self.parent.interpret(context)
        if isinstance(doc, Document) :
            return doc.getMember(context, self.name)
        else:
            raise InvalidDataError("Expecting a document, got:" + type(doc).__name__)
