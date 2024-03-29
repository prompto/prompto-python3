from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMethods(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAbstractMember(self):
        self.compareResourceOEO("methods/abstractMember.poc")

    def testAbstractMemberItem(self):
        self.compareResourceOEO("methods/abstractMemberItem.poc")

    def testAnonymous(self):
        self.compareResourceOEO("methods/anonymous.poc")

    def testAttribute(self):
        self.compareResourceOEO("methods/attribute.poc")

    def testDefault(self):
        self.compareResourceOEO("methods/default.poc")

    def testE_as_e_bug(self):
        self.compareResourceOEO("methods/e_as_e_bug.poc")

    def testEmpty(self):
        self.compareResourceOEO("methods/empty.poc")

    def testExplicit(self):
        self.compareResourceOEO("methods/explicit.poc")

    def testExplicitMember(self):
        self.compareResourceOEO("methods/explicitMember.poc")

    def testExpressionMember(self):
        self.compareResourceOEO("methods/expressionMember.poc")

    def testExpressionWith(self):
        self.compareResourceOEO("methods/expressionWith.poc")

    def testExtended(self):
        self.compareResourceOEO("methods/extended.poc")

    def testGlobal(self):
        self.compareResourceOEO("methods/global.poc")

    def testHomonym2(self):
        self.compareResourceOEO("methods/homonym2.poc")

    def testInheritedMember(self):
        self.compareResourceOEO("methods/inheritedMember.poc")

    def testLocalMember(self):
        self.compareResourceOEO("methods/localMember.poc")

    def testMember(self):
        self.compareResourceOEO("methods/member.poc")

    def testMemberRef(self):
        self.compareResourceOEO("methods/memberRef.poc")

    def testOverride(self):
        self.compareResourceOEO("methods/override.poc")

    def testParameter(self):
        self.compareResourceOEO("methods/parameter.poc")

    def testPolymorphicAbstract(self):
        self.compareResourceOEO("methods/polymorphicAbstract.poc")

    def testPolymorphicMember(self):
        self.compareResourceOEO("methods/polymorphicMember.poc")

    def testPolymorphicNamed(self):
        self.compareResourceOEO("methods/polymorphicNamed.poc")

    def testPolymorphicRuntime(self):
        self.compareResourceOEO("methods/polymorphicRuntime.poc")

    def testReturn(self):
        self.compareResourceOEO("methods/return.poc")

    def testSpecified(self):
        self.compareResourceOEO("methods/specified.poc")

    def testTextAsync(self):
        self.compareResourceOEO("methods/textAsync.poc")

    def testVoidAsync(self):
        self.compareResourceOEO("methods/voidAsync.poc")


