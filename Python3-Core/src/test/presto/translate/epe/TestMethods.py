from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceEPE("methods/anonymous.e")

    def testAttribute(self):
        self.compareResourceEPE("methods/attribute.e")

    def testDefault(self):
        self.compareResourceEPE("methods/default.e")

    def testE_as_e_bug(self):
        self.compareResourceEPE("methods/e_as_e_bug.e")

    def testExpressionWith(self):
        self.compareResourceEPE("methods/expressionWith.e")

    def testImplicit(self):
        self.compareResourceEPE("methods/implicit.e")

    def testMember(self):
        self.compareResourceEPE("methods/member.e")

    def testPolymorphic_abstract(self):
        self.compareResourceEPE("methods/polymorphic_abstract.e")

    def testPolymorphic_implicit(self):
        self.compareResourceEPE("methods/polymorphic_implicit.e")

    def testPolymorphic_named(self):
        self.compareResourceEPE("methods/polymorphic_named.e")

    def testPolymorphic_runtime(self):
        self.compareResourceEPE("methods/polymorphic_runtime.e")

    def testReturn(self):
        self.compareResourceEPE("methods/return.e")

    def testSpecified(self):
        self.compareResourceEPE("methods/specified.e")


