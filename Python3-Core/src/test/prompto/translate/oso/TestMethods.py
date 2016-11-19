from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceOSO("methods/anonymous.poc")

    def testAttribute(self):
        self.compareResourceOSO("methods/attribute.poc")

    def testDefault(self):
        self.compareResourceOSO("methods/default.poc")

    def testE_as_e_bug(self):
        self.compareResourceOSO("methods/e_as_e_bug.poc")

    def testExplicit(self):
        self.compareResourceOSO("methods/explicit.poc")

    def testExpressionWith(self):
        self.compareResourceOSO("methods/expressionWith.poc")

    def testExtended(self):
        self.compareResourceOSO("methods/extended.poc")

    def testImplicit(self):
        self.compareResourceOSO("methods/implicit.poc")

    def testMember(self):
        self.compareResourceOSO("methods/member.poc")

    def testPolymorphic_abstract(self):
        self.compareResourceOSO("methods/polymorphic_abstract.poc")

    def testPolymorphic_implicit(self):
        self.compareResourceOSO("methods/polymorphic_implicit.poc")

    def testPolymorphic_named(self):
        self.compareResourceOSO("methods/polymorphic_named.poc")

    def testPolymorphic_runtime(self):
        self.compareResourceOSO("methods/polymorphic_runtime.poc")

    def testReturn(self):
        self.compareResourceOSO("methods/return.poc")

    def testSpecified(self):
        self.compareResourceOSO("methods/specified.poc")


