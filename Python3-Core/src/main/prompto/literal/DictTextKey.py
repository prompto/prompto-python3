from prompto.utils.StringUtils import unescape

class DictTextKey(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def asText(self):
        from prompto.value.Text import Text
        s = unescape(self.text)
        return Text(s)

