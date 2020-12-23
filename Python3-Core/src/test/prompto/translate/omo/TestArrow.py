from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestArrow(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testArrowArgument(self):
        self.compareResourceOMO("arrow/arrowArgument.poc")

    def testFilterFromList(self):
        self.compareResourceOMO("arrow/filterFromList.poc")

    def testFilterFromSet(self):
        self.compareResourceOMO("arrow/filterFromSet.poc")

    def testHasAllFromList(self):
        self.compareResourceOMO("arrow/hasAllFromList.poc")

    def testHasAllFromSet(self):
        self.compareResourceOMO("arrow/hasAllFromSet.poc")

    def testHasAnyFromList(self):
        self.compareResourceOMO("arrow/hasAnyFromList.poc")

    def testHasAnyFromSet(self):
        self.compareResourceOMO("arrow/hasAnyFromSet.poc")

    def testSortCategory1Arg(self):
        self.compareResourceOMO("arrow/sortCategory1Arg.poc")

    def testSortCategory2Args(self):
        self.compareResourceOMO("arrow/sortCategory2Args.poc")

    def testSortText1Arg(self):
        self.compareResourceOMO("arrow/sortText1Arg.poc")

    def testSortText1ArgDesc(self):
        self.compareResourceOMO("arrow/sortText1ArgDesc.poc")

    def testSortText2Args(self):
        self.compareResourceOMO("arrow/sortText2Args.poc")

    def testSortText2ArgsDesc(self):
        self.compareResourceOMO("arrow/sortText2ArgsDesc.poc")


