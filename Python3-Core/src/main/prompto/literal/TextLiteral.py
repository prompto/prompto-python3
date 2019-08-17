from prompto.literal.Literal import Literal
from prompto.type.TextType import TextType
from prompto.utils.StringUtils import unescape

class TextLiteral(Literal):

    def __init__(self, text):
        from prompto.value.Text import Text
        s = unescape(text)
        value = Text(s)
        super().__init__(text, value)

    def check(self, context):
        return TextType.instance
