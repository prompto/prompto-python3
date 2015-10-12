from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceOEO("methods/anonymous.poc")

    def testAttribute(self):
        self.compareResourceOEO("methods/attribute.poc")

    def testDefault(self):
        self.compareResourceOEO("methods/default.poc")

    def testE_as_e_bug(self):
        self.compareResourceOEO("methods/e_as_e_bug.poc")

    def testExpressionWith(self):
        self.compareResourceOEO("methods/expressionWith.poc")

    def testImplicit(self):
        self.compareResourceOEO("methods/implicit.poc")

    def testMember(self):
        self.compareResourceOEO("methods/member.poc")

    def testPolymorphic_abstract(self):
        self.compareResourceOEO("methods/polymorphic_abstract.poc")

    def testPolymorphic_implicit(self):
        self.compareResourceOEO("methods/polymorphic_implicit.poc")

    def testPolymorphic_named(self):
        self.compareResourceOEO("methods/polymorphic_named.poc")

    def testPolymorphic_runtime(self):
        self.compareResourceOEO("methods/polymorphic_runtime.poc")

    def testReturn(self):
        self.compareResourceOEO("methods/return.poc")

    def testSpecified(self):
        self.compareResourceOEO("methods/specified.poc")


