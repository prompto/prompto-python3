from prompto.value.Boolean import Boolean

# a utility class for running unit tests only
class MemStore(object):

    instance = None

    def __init__(self):
        self.instances = set()

    def store (self,  document):
        self.instances.add (document)

    def fetchOne (self, context, xfilter):
        for doc in self.instances:
            local = context.newDocumentContext (doc)
            test = xfilter.interpret (local)
            if not isinstance(test, Boolean):
                raise InternalError ("Illegal test result: " + test)
            if test.value:
                return doc
        return None\

MemStore.instance = MemStore ()