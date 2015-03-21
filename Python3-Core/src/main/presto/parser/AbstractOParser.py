from presto.parser.AbstractParser import AbstractParser

# this is just to enable per dialect downcasting in the Java/C# runtimes
class AbstractOParser(AbstractParser):

    def __init__(self, input_):
        super().__init__(input_)
