from presto.error.InvalidDataError import InvalidDataError
from presto.grammar.IAttributeConstraint import IAttributeConstraint
from presto.value.IContainer import IContainer


class MatchingCollectionConstraint ( IAttributeConstraint ):

    def __init__(self, collection):
        super(MatchingCollectionConstraint, self).__init__()
        self.collection = collection

    def checkValue(self, context, value):
        container = self.collection.interpret(context)
        if isinstance(container, IContainer):
            if not container.hasItem(context, value):
                raise InvalidDataError("Value:" + str(value) + " is not in range: " + str(self.collection))
        else:
            raise InvalidDataError("Not a collection: " + self.collection.toString())

    def toDialect(self, writer):
        writer.append(" in ")
        self.collection.toDialect(writer)
