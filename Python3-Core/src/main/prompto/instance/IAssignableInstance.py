class IAssignableInstance ( object ):

    def checkAssignValue(self, context, valueType):
        raise "Must override!"


    def checkAssignMember(self, context, name, valueType):
        raise "Must override!"


    def checkAssignItem(self, context, itemType, valueType):
        raise "Must override!"