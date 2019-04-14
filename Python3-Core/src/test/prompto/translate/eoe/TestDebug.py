from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDebug(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testStack(self):
        self.compareResourceEOE("debug/stack.pec")

    def testVariable_boolean(self):
        self.compareResourceEOE("debug/variable-boolean.pec")

    def testVariable_category(self):
        self.compareResourceEOE("debug/variable-category.pec")

    def testVariable_character(self):
        self.compareResourceEOE("debug/variable-character.pec")

    def testVariable_css(self):
        self.compareResourceEOE("debug/variable-css.pec")

    def testVariable_cursor(self):
        self.compareResourceEOE("debug/variable-cursor.pec")

    def testVariable_date(self):
        self.compareResourceEOE("debug/variable-date.pec")

    def testVariable_dateTime(self):
        self.compareResourceEOE("debug/variable-dateTime.pec")

    def testVariable_decimal(self):
        self.compareResourceEOE("debug/variable-decimal.pec")

    def testVariable_dictionary(self):
        self.compareResourceEOE("debug/variable-dictionary.pec")

    def testVariable_document(self):
        self.compareResourceEOE("debug/variable-document.pec")

    def testVariable_integer(self):
        self.compareResourceEOE("debug/variable-integer.pec")

    def testVariable_iterator(self):
        self.compareResourceEOE("debug/variable-iterator.pec")

    def testVariable_list(self):
        self.compareResourceEOE("debug/variable-list.pec")

    def testVariable_null(self):
        self.compareResourceEOE("debug/variable-null.pec")

    def testVariable_range(self):
        self.compareResourceEOE("debug/variable-range.pec")

    def testVariable_set(self):
        self.compareResourceEOE("debug/variable-set.pec")

    def testVariable_text(self):
        self.compareResourceEOE("debug/variable-text.pec")

    def testVariable_time(self):
        self.compareResourceEOE("debug/variable-time.pec")

    def testVariable_tuple(self):
        self.compareResourceEOE("debug/variable-tuple.pec")

    def testVariable_uuid(self):
        self.compareResourceEOE("debug/variable-uuid.pec")

    def testVariable_version(self):
        self.compareResourceEOE("debug/variable-version.pec")

    def testVariables(self):
        self.compareResourceEOE("debug/variables.pec")


