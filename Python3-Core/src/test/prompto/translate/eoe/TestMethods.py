from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceEOE("methods/anonymous.pec")

    def testAttribute(self):
        self.compareResourceEOE("methods/attribute.pec")

    def testDefault(self):
        self.compareResourceEOE("methods/default.pec")

    def testE_as_e_bug(self):
        self.compareResourceEOE("methods/e_as_e_bug.pec")

    def testExplicit(self):
        self.compareResourceEOE("methods/explicit.pec")

    def testExpressionWith(self):
        self.compareResourceEOE("methods/expressionWith.pec")

    def testExtended(self):
        self.compareResourceEOE("methods/extended.pec")

    def testHomonym(self):
        self.compareResourceEOE("methods/homonym.pec")

    def testImplicitMember(self):
        self.compareResourceEOE("methods/implicitMember.pec")

    def testMember(self):
        self.compareResourceEOE("methods/member.pec")

    def testMemberCall(self):
        self.compareResourceEOE("methods/memberCall.pec")

    def testOverride(self):
        self.compareResourceEOE("methods/override.pec")

    def testPolymorphic_abstract(self):
        self.compareResourceEOE("methods/polymorphic_abstract.pec")

    def testPolymorphic_implicit(self):
        self.compareResourceEOE("methods/polymorphic_implicit.pec")

    def testPolymorphic_named(self):
        self.compareResourceEOE("methods/polymorphic_named.pec")

    def testPolymorphic_runtime(self):
        self.compareResourceEOE("methods/polymorphic_runtime.pec")

    def testReturn(self):
        self.compareResourceEOE("methods/return.pec")

    def testSpecified(self):
        self.compareResourceEOE("methods/specified.pec")


