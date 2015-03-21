from io import StringIO

class ObjectList ( list ):

    def __init__(self, items = None):
        super(ObjectList, self).__init__()
        if items is not None:
            self.extend(items)

    def __str__(self):
        sb = StringIO()
        for item in self:
            sb.write(str(item))
            sb.write(", " )
        return sb.getvalue()[:-2]
