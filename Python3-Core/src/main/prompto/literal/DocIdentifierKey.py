
class DocIdentifierKey(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        return TextValue(self.name)
