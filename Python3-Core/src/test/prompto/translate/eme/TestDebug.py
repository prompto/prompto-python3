from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDebug(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testStack(self):
        self.compareResourceEME("debug/stack.pec")

    def testVariable_boolean(self):
        self.compareResourceEME("debug/variable-boolean.pec")

    def testVariable_category(self):
        self.compareResourceEME("debug/variable-category.pec")

    def testVariable_character(self):
        self.compareResourceEME("debug/variable-character.pec")

    def testVariable_css(self):
        self.compareResourceEME("debug/variable-css.pec")

    def testVariable_cursor(self):
        self.compareResourceEME("debug/variable-cursor.pec")

    def testVariable_date(self):
        self.compareResourceEME("debug/variable-date.pec")

    def testVariable_dateTime(self):
        self.compareResourceEME("debug/variable-dateTime.pec")

    def testVariable_decimal(self):
        self.compareResourceEME("debug/variable-decimal.pec")

    def testVariable_dictionary(self):
        self.compareResourceEME("debug/variable-dictionary.pec")

    def testVariable_document(self):
        self.compareResourceEME("debug/variable-document.pec")

    def testVariable_integer(self):
        self.compareResourceEME("debug/variable-integer.pec")

    def testVariable_iterator(self):
        self.compareResourceEME("debug/variable-iterator.pec")

    def testVariable_list(self):
        self.compareResourceEME("debug/variable-list.pec")

    def testVariable_null(self):
        self.compareResourceEME("debug/variable-null.pec")

    def testVariable_range(self):
        self.compareResourceEME("debug/variable-range.pec")

    def testVariable_set(self):
        self.compareResourceEME("debug/variable-set.pec")

    def testVariable_text(self):
        self.compareResourceEME("debug/variable-text.pec")

    def testVariable_time(self):
        self.compareResourceEME("debug/variable-time.pec")

    def testVariable_tuple(self):
        self.compareResourceEME("debug/variable-tuple.pec")

    def testVariable_uuid(self):
        self.compareResourceEME("debug/variable-uuid.pec")

    def testVariable_version(self):
        self.compareResourceEME("debug/variable-version.pec")

    def testVariables(self):
        self.compareResourceEME("debug/variables.pec")


