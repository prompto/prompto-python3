from prompto.python.PythonExpression import PythonExpression

class PythonSelectorExpression(PythonExpression):

    def __init__(self):
        self.parent = None

    def setParent(self, parent):
        self.parent = parent

