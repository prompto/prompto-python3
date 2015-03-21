from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnonymous(self):
        self.checkOutput("methods/anonymous.o")

    def testAttribute(self):
        self.checkOutput("methods/attribute.o")

    def testDefault(self):
        self.checkOutput("methods/default.o")

    def testE_as_e_bug(self):
        self.checkOutput("methods/e_as_e_bug.o")

    def testExpressionWith(self):
        self.checkOutput("methods/expressionWith.o")

    def testImplicit(self):
        self.checkOutput("methods/implicit.o")

    def testMember(self):
        self.checkOutput("methods/member.o")

    def testPolymorphic_abstract(self):
        self.checkOutput("methods/polymorphic_abstract.o")

    def testPolymorphic_implicit(self):
        self.checkOutput("methods/polymorphic_implicit.o")

    def testPolymorphic_named(self):
        self.checkOutput("methods/polymorphic_named.o")

    def testPolymorphic_runtime(self):
        self.checkOutput("methods/polymorphic_runtime.o")

    def testSpecified(self):
        self.checkOutput("methods/specified.o")


