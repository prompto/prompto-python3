from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceEOE("methods/anonymous.e")

    def testAttribute(self):
        self.compareResourceEOE("methods/attribute.e")

    def testDefault(self):
        self.compareResourceEOE("methods/default.e")

    def testE_as_e_bug(self):
        self.compareResourceEOE("methods/e_as_e_bug.e")

    def testExpressionWith(self):
        self.compareResourceEOE("methods/expressionWith.e")

    def testImplicit(self):
        self.compareResourceEOE("methods/implicit.e")

    def testMember(self):
        self.compareResourceEOE("methods/member.e")

    def testPolymorphic_abstract(self):
        self.compareResourceEOE("methods/polymorphic_abstract.e")

    def testPolymorphic_implicit(self):
        self.compareResourceEOE("methods/polymorphic_implicit.e")

    def testPolymorphic_named(self):
        self.compareResourceEOE("methods/polymorphic_named.e")

    def testPolymorphic_runtime(self):
        self.compareResourceEOE("methods/polymorphic_runtime.e")

    def testReturn(self):
        self.compareResourceEOE("methods/return.e")

    def testSpecified(self):
        self.compareResourceEOE("methods/specified.e")


