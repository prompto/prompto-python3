from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceOMO("methods/anonymous.poc")

    def testAttribute(self):
        self.compareResourceOMO("methods/attribute.poc")

    def testDefault(self):
        self.compareResourceOMO("methods/default.poc")

    def testE_as_e_bug(self):
        self.compareResourceOMO("methods/e_as_e_bug.poc")

    def testExplicit(self):
        self.compareResourceOMO("methods/explicit.poc")

    def testExplicitMember(self):
        self.compareResourceOMO("methods/explicitMember.poc")

    def testExpressionWith(self):
        self.compareResourceOMO("methods/expressionWith.poc")

    def testExtended(self):
        self.compareResourceOMO("methods/extended.poc")

    def testGlobal(self):
        self.compareResourceOMO("methods/global.poc")

    def testImplicitMember(self):
        self.compareResourceOMO("methods/implicitMember.poc")

    def testMember(self):
        self.compareResourceOMO("methods/member.poc")

    def testOverride(self):
        self.compareResourceOMO("methods/override.poc")

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


