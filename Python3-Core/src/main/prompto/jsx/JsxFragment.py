from prompto.jsx.IJsxExpression import IJsxExpression
from prompto.type.JsxType import JsxType


class JsxFragment(IJsxExpression):

    def __init__(self, openingSuite:str):
        super().__init__()
        self.openingSuite = openingSuite
        self.children = []


    def toDialect(self, writer):
        writer.append("<>")
        if self.openingSuite is not None:
            writer.appendRaw(self.openingSuite)
        if self.children is not None:
            [ child.toDialect(writer) for child in self.children]
        writer.append("</>")


    def check(self, context):
        if self.children is not None:
            [child.check(context) for child in self.children]
        return JsxType.instance
