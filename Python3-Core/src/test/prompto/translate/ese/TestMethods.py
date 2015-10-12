from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnonymous(self):
        self.compareResourceESE("methods/anonymous.pec")

    def testAttribute(self):
        self.compareResourceESE("methods/attribute.pec")

    def testDefault(self):
        self.compareResourceESE("methods/default.pec")

    def testE_as_e_bug(self):
        self.compareResourceESE("methods/e_as_e_bug.pec")

    def testExpressionWith(self):
        self.compareResourceESE("methods/expressionWith.pec")

    def testImplicit(self):
        self.compareResourceESE("methods/implicit.pec")

    def testMember(self):
        self.compareResourceESE("methods/member.pec")

    def testMemberCall(self):
        self.compareResourceESE("methods/memberCall.pec")

    def testPolymorphic_abstract(self):
        self.compareResourceESE("methods/polymorphic_abstract.pec")

    def testPolymorphic_implicit(self):
        self.compareResourceESE("methods/polymorphic_implicit.pec")

    def testPolymorphic_named(self):
        self.compareResourceESE("methods/polymorphic_named.pec")

    def testPolymorphic_runtime(self):
        self.compareResourceESE("methods/polymorphic_runtime.pec")

    def testReturn(self):
        self.compareResourceESE("methods/return.pec")

    def testSpecified(self):
        self.compareResourceESE("methods/specified.pec")


