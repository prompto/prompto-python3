from prompto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration

class AnyNativeCategoryDeclaration(NativeCategoryDeclaration):

    def __init__(self):
        super().__init__("Any", [], [], [], [])

AnyNativeCategoryDeclaration.instance = AnyNativeCategoryDeclaration()
