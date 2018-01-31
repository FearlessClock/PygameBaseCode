class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toArray(self):
        return [self.x, self.y]

    def toTuple(self):
        return (self.x, self.y)

    def __str__(self):
        return "("+str(self.x) + ":" + str(self.y)+")"