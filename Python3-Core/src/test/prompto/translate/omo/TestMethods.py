from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAbstractMember(self):
        self.compareResourceOMO("methods/abstractMember.poc")

    def testAnonymous(self):
        self.compareResourceOMO("methods/anonymous.poc")

    def testAttribute(self):
        self.compareResourceOMO("methods/attribute.poc")

    def testDefault(self):
        self.compareResourceOMO("methods/default.poc")

    def testE_as_e_bug(self):
        self.compareResourceOMO("methods/e_as_e_bug.poc")

    def testEmpty(self):
        self.compareResourceOMO("methods/empty.poc")

    def testExplicit(self):
        self.compareResourceOMO("methods/explicit.poc")

    def testExplicitMember(self):
        self.compareResourceOMO("methods/explicitMember.poc")

    def testExpressionMember(self):
        self.compareResourceOMO("methods/expressionMember.poc")

    def testExpressionWith(self):
        self.compareResourceOMO("methods/expressionWith.poc")

    def testExtended(self):
        self.compareResourceOMO("methods/extended.poc")

    def testGlobal(self):
        self.compareResourceOMO("methods/global.poc")

    def testHomonym2(self):
        self.compareResourceOMO("methods/homonym2.poc")

    def testImplicitMember(self):
        self.compareResourceOMO("methods/implicitMember.poc")

    def testMember(self):
        self.compareResourceOMO("methods/member.poc")

    def testMemberRef(self):
        self.compareResourceOMO("methods/memberRef.poc")

    def testOverride(self):
        self.compareResourceOMO("methods/override.poc")

    def testParameter(self):
        self.compareResourceOMO("methods/parameter.poc")

    def testPolymorphic_abstract(self):
        self.compareResourceOMO("methods/polymorphic_abstract.poc")

    def testPolymorphic_implicit(self):
        self.compareResourceOMO("methods/polymorphic_implicit.poc")

    def testPolymorphic_named(self):
        self.compareResourceOMO("methods/polymorphic_named.poc")

    def testPolymorphic_runtime(self):
        self.compareResourceOMO("methods/polymorphic_runtime.poc")

    def testReturn(self):
        self.compareResourceOMO("methods/return.poc")

    def testSpecified(self):
        self.compareResourceOMO("methods/specified.poc")

    def testTextAsync(self):
        self.compareResourceOMO("methods/textAsync.poc")

    def testVoidAsync(self):
        self.compareResourceOMO("methods/voidAsync.poc")


