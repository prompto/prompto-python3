from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestArrow(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testArrowArgument(self):
        self.compareResourceOEO("arrow/arrowArgument.poc")

    def testFilterFromList(self):
        self.compareResourceOEO("arrow/filterFromList.poc")

    def testFilterFromSet(self):
        self.compareResourceOEO("arrow/filterFromSet.poc")

    def testSortCategory1Arg(self):
        self.compareResourceOEO("arrow/sortCategory1Arg.poc")

    def testSortCategory2Args(self):
        self.compareResourceOEO("arrow/sortCategory2Args.poc")

    def testSortText1Arg(self):
        self.compareResourceOEO("arrow/sortText1Arg.poc")

    def testSortText1ArgDesc(self):
        self.compareResourceOEO("arrow/sortText1ArgDesc.poc")

    def testSortText2Args(self):
        self.compareResourceOEO("arrow/sortText2Args.poc")

    def testSortText2ArgsDesc(self):
        self.compareResourceOEO("arrow/sortText2ArgsDesc.poc")


