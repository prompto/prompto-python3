from prompto.value.Document import Document

class StorableDocument(object):

    def __init__(self):
        self.document = None

    def __getattribute__(self, key):
        if key=="dirty":
            return self.document is not None
        else:
            return object.__getattribute__(self, key)

    def __setattr__(self, key, value):
        if key=="dirty":
            if value==False:
                self.document = None
            else:
                self.document = Document()
        else:
            self.__dict__[key] = value

    def  asDocument (self):
        return self.document


    def SetMember (self, context, name, value):
        if self.document is None:
            self.document = Document()
        self.document.SetMember (context, name, value);
