from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCast(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceOMO("cast/autoDowncast.poc")

    def testAutoDowncastMethod(self):
        self.compareResourceOMO("cast/autoDowncastMethod.poc")

    def testCastChild(self):
        self.compareResourceOMO("cast/castChild.poc")

    def testCastEnum(self):
        self.compareResourceOMO("cast/castEnum.poc")

    def testCastMethod(self):
        self.compareResourceOMO("cast/castMethod.poc")

    def testCastMissing(self):
        self.compareResourceOMO("cast/castMissing.poc")

    def testCastNull(self):
        self.compareResourceOMO("cast/castNull.poc")

    def testCastParent(self):
        self.compareResourceOMO("cast/castParent.poc")

    def testIsAChild(self):
        self.compareResourceOMO("cast/isAChild.poc")

    def testIsAText(self):
        self.compareResourceOMO("cast/isAText.poc")

    def testMutableEntity(self):
        self.compareResourceOMO("cast/mutableEntity.poc")

    def testMutableList(self):
        self.compareResourceOMO("cast/mutableList.poc")

    def testNullIsNotAText(self):
        self.compareResourceOMO("cast/nullIsNotAText.poc")


