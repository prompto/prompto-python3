from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAbstractMember(self):
        self.compareResourceEOE("methods/abstractMember.pec")

    def testAnonymous(self):
        self.compareResourceEOE("methods/anonymous.pec")

    def testAttribute(self):
        self.compareResourceEOE("methods/attribute.pec")

    def testDefault(self):
        self.compareResourceEOE("methods/default.pec")

    def testE_as_e_bug(self):
        self.compareResourceEOE("methods/e_as_e_bug.pec")

    def testEmpty(self):
        self.compareResourceEOE("methods/empty.pec")

    def testExplicit(self):
        self.compareResourceEOE("methods/explicit.pec")

    def testExplicitMember(self):
        self.compareResourceEOE("methods/explicitMember.pec")

    def testExpressionMember(self):
        self.compareResourceEOE("methods/expressionMember.pec")

    def testExpressionWith(self):
        self.compareResourceEOE("methods/expressionWith.pec")

    def testExtended(self):
        self.compareResourceEOE("methods/extended.pec")

    def testGlobal(self):
        self.compareResourceEOE("methods/global.pec")

    def testHomonym(self):
        self.compareResourceEOE("methods/homonym.pec")

    def testHomonym2(self):
        self.compareResourceEOE("methods/homonym2.pec")

    def testImplicitAnd(self):
        self.compareResourceEOE("methods/implicitAnd.pec")

    def testMember(self):
        self.compareResourceEOE("methods/member.pec")

    def testMemberCall(self):
        self.compareResourceEOE("methods/memberCall.pec")

    def testMemberRef(self):
        self.compareResourceEOE("methods/memberRef.pec")

    def testOverride(self):
        self.compareResourceEOE("methods/override.pec")

    def testParameter(self):
        self.compareResourceEOE("methods/parameter.pec")

    def testPolymorphicAbstract(self):
        self.compareResourceEOE("methods/polymorphicAbstract.pec")

    def testPolymorphicMember(self):
        self.compareResourceEOE("methods/polymorphicMember.pec")

    def testPolymorphicNamed(self):
        self.compareResourceEOE("methods/polymorphicNamed.pec")

    def testPolymorphicRuntime(self):
        self.compareResourceEOE("methods/polymorphicRuntime.pec")

    def testReturn(self):
        self.compareResourceEOE("methods/return.pec")

    def testSpecified(self):
        self.compareResourceEOE("methods/specified.pec")

    def testTextAsync(self):
        self.compareResourceEOE("methods/textAsync.pec")

    def testVoidAsync(self):
        self.compareResourceEOE("methods/voidAsync.pec")


