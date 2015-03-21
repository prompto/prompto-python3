# used to ensure downcast local resolves to actual value */
class LinkedValue(object):

    def __init__(self, context):
        self.context = context
