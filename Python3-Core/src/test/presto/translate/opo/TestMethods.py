from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceOPO("methods/anonymous.o")

    def testAttribute(self):
        self.compareResourceOPO("methods/attribute.o")

    def testDefault(self):
        self.compareResourceOPO("methods/default.o")

    def testE_as_e_bug(self):
        self.compareResourceOPO("methods/e_as_e_bug.o")

    def testExpressionWith(self):
        self.compareResourceOPO("methods/expressionWith.o")

    def testImplicit(self):
        self.compareResourceOPO("methods/implicit.o")

    def testMember(self):
        self.compareResourceOPO("methods/member.o")

    def testPolymorphic_abstract(self):
        self.compareResourceOPO("methods/polymorphic_abstract.o")

    def testPolymorphic_implicit(self):
        self.compareResourceOPO("methods/polymorphic_implicit.o")

    def testPolymorphic_named(self):
        self.compareResourceOPO("methods/polymorphic_named.o")

    def testPolymorphic_runtime(self):
        self.compareResourceOPO("methods/polymorphic_runtime.o")

    def testReturn(self):
        self.compareResourceOPO("methods/return.o")

    def testSpecified(self):
        self.compareResourceOPO("methods/specified.o")


