from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAbstractMember(self):
        self.checkOutput("methods/abstractMember.poc")

    def testAnonymous(self):
        self.checkOutput("methods/anonymous.poc")

    def testAttribute(self):
        self.checkOutput("methods/attribute.poc")

    def testDefault(self):
        self.checkOutput("methods/default.poc")

    def testE_as_e_bug(self):
        self.checkOutput("methods/e_as_e_bug.poc")

    def testExplicit(self):
        self.checkOutput("methods/explicit.poc")

    def testExplicitMember(self):
        self.checkOutput("methods/explicitMember.poc")

    def testExpressionMember(self):
        self.checkOutput("methods/expressionMember.poc")

    def testExpressionWith(self):
        self.checkOutput("methods/expressionWith.poc")

    def testExtended(self):
        self.checkOutput("methods/extended.poc")

    def testHomonym2(self):
        self.checkOutput("methods/homonym2.poc")

    def testMember(self):
        self.checkOutput("methods/member.poc")

    def testMemberRef(self):
        self.checkOutput("methods/memberRef.poc")

    def testOverride(self):
        self.checkOutput("methods/override.poc")

    def testParameter(self):
        self.checkOutput("methods/parameter.poc")

    def testPolymorphic_abstract(self):
        self.checkOutput("methods/polymorphic_abstract.poc")

    def testPolymorphic_named(self):
        self.checkOutput("methods/polymorphic_named.poc")

    def testPolymorphic_runtime(self):
        self.checkOutput("methods/polymorphic_runtime.poc")

    def testSpecified(self):
        self.checkOutput("methods/specified.poc")

    def testTextAsync(self):
        self.checkOutput("methods/textAsync.poc")

    def testVoidAsync(self):
        self.checkOutput("methods/voidAsync.poc")


