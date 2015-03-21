from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceOEO("methods/anonymous.o")

    def testAttribute(self):
        self.compareResourceOEO("methods/attribute.o")

    def testDefault(self):
        self.compareResourceOEO("methods/default.o")

    def testE_as_e_bug(self):
        self.compareResourceOEO("methods/e_as_e_bug.o")

    def testExpressionWith(self):
        self.compareResourceOEO("methods/expressionWith.o")

    def testImplicit(self):
        self.compareResourceOEO("methods/implicit.o")

    def testMember(self):
        self.compareResourceOEO("methods/member.o")

    def testPolymorphic_abstract(self):
        self.compareResourceOEO("methods/polymorphic_abstract.o")

    def testPolymorphic_implicit(self):
        self.compareResourceOEO("methods/polymorphic_implicit.o")

    def testPolymorphic_named(self):
        self.compareResourceOEO("methods/polymorphic_named.o")

    def testPolymorphic_runtime(self):
        self.compareResourceOEO("methods/polymorphic_runtime.o")

    def testReturn(self):
        self.compareResourceOEO("methods/return.o")

    def testSpecified(self):
        self.compareResourceOEO("methods/specified.o")


