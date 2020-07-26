class ApplicationContext(object):

    instance = None

    @staticmethod
    def set(context):
        current = ApplicationContext.instance
        ApplicationContext.instance = context
        return current

    @staticmethod
    def get():
        return ApplicationContext.instance