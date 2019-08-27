from prompto.jsx.IJsxExpression import IJsxExpression
from prompto.type.JsxType import JsxType


class JsxElementBase(IJsxExpression):

    def __init__(self, name, properties):
        super().__init__()
        self.name = name
        self.properties = properties


    def check(self, context):
        if self.properties is not None:
            for prop in self.properties:
                prop.check(context)
        return JsxType.instance


