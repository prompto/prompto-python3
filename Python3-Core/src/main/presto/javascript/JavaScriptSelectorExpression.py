from presto.javascript.JavaScriptExpression import JavaScriptExpression


class JavaScriptSelectorExpression (JavaScriptExpression):

    def __init__(self, parent = None):
        self.parent = parent
