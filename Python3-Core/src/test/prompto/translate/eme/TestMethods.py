from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceEME("methods/anonymous.pec")

    def testAttribute(self):
        self.compareResourceEME("methods/attribute.pec")

    def testDefault(self):
        self.compareResourceEME("methods/default.pec")

    def testE_as_e_bug(self):
        self.compareResourceEME("methods/e_as_e_bug.pec")

    def testEmpty(self):
        self.compareResourceEME("methods/empty.pec")

    def testExplicit(self):
        self.compareResourceEME("methods/explicit.pec")

    def testExplicitMember(self):
        self.compareResourceEME("methods/explicitMember.pec")

    def testExpressionMember(self):
        self.compareResourceEME("methods/expressionMember.pec")

    def testExpressionWith(self):
        self.compareResourceEME("methods/expressionWith.pec")

    def testExtended(self):
        self.compareResourceEME("methods/extended.pec")

    def testGlobal(self):
        self.compareResourceEME("methods/global.pec")

    def testHomonym(self):
        self.compareResourceEME("methods/homonym.pec")

    def testImplicitAnd(self):
        self.compareResourceEME("methods/implicitAnd.pec")

    def testImplicitMember(self):
        self.compareResourceEME("methods/implicitMember.pec")

    def testMember(self):
        self.compareResourceEME("methods/member.pec")

    def testMemberCall(self):
        self.compareResourceEME("methods/memberCall.pec")

    def testOverride(self):
        self.compareResourceEME("methods/override.pec")

    def testPolymorphic_abstract(self):
        self.compareResourceEME("methods/polymorphic_abstract.pec")

    def testPolymorphic_implicit(self):
        self.compareResourceEME("methods/polymorphic_implicit.pec")

    def testPolymorphic_named(self):
        self.compareResourceEME("methods/polymorphic_named.pec")

    def testPolymorphic_runtime(self):
        self.compareResourceEME("methods/polymorphic_runtime.pec")

    def testReturn(self):
        self.compareResourceEME("methods/return.pec")

    def testSpecified(self):
        self.compareResourceEME("methods/specified.pec")

    def testTextAsync(self):
        self.compareResourceEME("methods/textAsync.pec")

    def testVoidAsync(self):
        self.compareResourceEME("methods/voidAsync.pec")


