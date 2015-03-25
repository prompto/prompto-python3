from presto.parser.Location import Location
from presto.parser.ISection import ISection

class Section(ISection):

    def __init__(self):
        self.path = None
        self.start = None
        self.end = None
        self.dialect = None
        self.breakpoint = None

    def setFrom(self, path, start, end, dialect):
        self.path = path
        self.start = Location(start)
        self.end = Location(end, True)
        self.dialect = dialect

    def getPath(self):
        return self.path

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def setAsBreakpoint(self, set_):
        self.breakpoint = set_

    def isBreakpoint(self):
        return self.breakpoint
