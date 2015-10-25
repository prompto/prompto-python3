from prompto.error.SyntaxError import SyntaxError
from prompto.value.Boolean import Boolean
from prompto.value.Integer import Integer
from prompto.value.Document import Document

# a utility class for running unit tests only
class MemStore(object):

    def __init__(self):
        self.documents = set()

    def store (self,  document):
        self.documents.add (document)

    def fetchOne (self, context, xfilter):
        for doc in self.documents:
            if self.matches(context, doc, xfilter):
                return doc
        return None

    def matches (self, context, doc, xfilter):
        if xfilter is None:
            return True
        local = context.newDocumentContext (doc)
        test = xfilter.interpret (local)
        if not isinstance(test, Boolean):
            raise InternalError ("Illegal test result: " + test)
        return test.value

    def fetchMany(self, context, start, end, xfilter, orderBy):
        docs = self.fetchManyDocs(context, start, end, xfilter, orderBy)
        # need the below to do more than iterate
        return DocumentIterator(docs)

    def fetchManyDocs(self, context, start, end, xfilter, orderBy):
        docs = self.filterDocs(context, xfilter)
        # sort if required
        docs = self.sort(context, docs, orderBy)
        # slice it if required
        docs = self.slice(context, docs, start, end)
        # done
        return docs

    def filterDocs(self, context, xfilter):
        # create list of filtered docs
        docs = list()
        for doc in self.documents:
            if self.matches(context, doc, xfilter):
                docs.append(doc)
        return docs

    def slice(self, context, docs, start, end):
        if len(docs)==0 or start is None:
            return docs
        startValue = None
        endValue = None
        if start is not None:
            value = start.interpret(context)
            if value is None:
                raise NullReferenceError()
            elif not isinstance(value, Integer):
                raise SyntaxError("Expecting an integer, got " + value.type.name)
            startValue = value.IntegerValue()
        if end is not None:
            value = end.interpret(context)
            if value is None:
                raise NullReferenceError()
            elif not isinstance(value, Integer):
                raise SyntaxError("Expecting an integer, got " + value.type.name)
            endValue = value.IntegerValue()
        if startValue is None or startValue < 1:
            startValue = 1
        if endValue is None or endValue > len(docs):
            endValue = len(docs)
        if startValue > len(docs) or startValue > endValue:
            return list()
        else:
            return docs[startValue - 1 : endValue]

    def sort(self, context, docs, orderBy):
        if orderBy is None:
            return docs
        # need a closure builder on a per clause basis
        def valueExtractor(clause):
            # build the closure to be returned
            def extractValue(doc):
                source = doc
                value = None
                for name in clause.names:
                    if not isinstance(source, Document):
                        return None
                    value = source.GetMember(context, name)
                    source = value
                return value
            return extractValue
        # sorts are guaranteed to be stable, so go through clauses in reverse order
        for clause in reversed(orderBy):
            docs = sorted(docs, key=valueExtractor(clause), reverse = clause.descending)
        return docs

class DocumentIterator(object):

    def __init__(self, docs):
        self.docs = docs

    def __len__(self):
        return len(self.docs)

    def __iter__(self):
        for doc in self.docs:
            yield doc