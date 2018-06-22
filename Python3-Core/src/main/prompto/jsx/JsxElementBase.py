from prompto.jsx.IJsxExpression import IJsxExpression

class JsxElementBase(IJsxExpression):

    def __init__(self, name, attributes):
        super().__init__()
        self.name = name
        self.attributes = attributes


    def check(self, context):
        if self.attributes is not None:
            for attribute in self.attributes:
                attribute.check(context)
        return JsxType.instance


