from prompto.utils.StringUtils import unescape

class DocTextKey(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        s = unescape(self.text)
        return TextValue(s)

